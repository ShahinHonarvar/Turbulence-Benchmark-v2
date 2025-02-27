def all_left_right_truncatable_prime(tp):
    res = list()
    x = tp[37]
    for n in range(2, x + 1):
        num = str(n)
        if num.count('0') != 0:
            continue
        for i in range(len(num)):
            for j in range(i + 1):
                front = int(num[j:i + 1])
                back = int(num[::-1][j:i + 1][::-1])
                if front + back == n and isPrime(front) and isPrime(back):
                    res.append(n)
    if not res:
        return []
    return sorted(res, reverse=True)

def isPrime(n):
    if n == 2:
        return True
    if n <= 1 or n % 2 == 0:
        return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True