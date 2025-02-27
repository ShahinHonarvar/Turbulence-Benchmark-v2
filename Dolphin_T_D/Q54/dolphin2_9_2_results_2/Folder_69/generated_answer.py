def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def is_right_truncatable_prime(n):
    trun = n
    while trun > 0:
        if not is_prime(trun):
            return False
        trun //= 10
    return True

def all_right_truncatable_prime(t):
    x = t[760]
    res = []
    for i in range(2, x):
        if is_right_truncatable_prime(i):
            res.append(i)
    res.sort(reverse=True)
    return res if len(res) > 0 else []