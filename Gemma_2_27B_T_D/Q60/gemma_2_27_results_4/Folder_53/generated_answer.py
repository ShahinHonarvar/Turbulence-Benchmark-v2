def all_left_right_truncatable_prime(data):
    x = data[86]
    primes = []
    for i in range(x, 1, -1):
        s = str(i)
        flag = True
        if '0' in s:
            continue
        for j in range(len(s)):
            if not (is_prime(int(s[:j + 1])) and is_prime(int(s[j:]))):
                flag = False
                break
        if flag:
            primes.append(i)
    return sorted(primes, reverse=True)

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True