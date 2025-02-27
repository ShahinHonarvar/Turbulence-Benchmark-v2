def all_left_truncatable_prime(t):
    x = t[370]
    res = []
    for i in range(2, x):
        if not any(('0' in str(i) for i in range(i, 10))):
            temp = i
            while temp > 1:
                if not is_prime(temp):
                    break
                temp //= 10
            else:
                res.append(i)
    res.sort(reverse=True)
    return res

def is_prime(n):
    if n == 2:
        return True
    if n <= 1 or n % 2 == 0:
        return False
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True