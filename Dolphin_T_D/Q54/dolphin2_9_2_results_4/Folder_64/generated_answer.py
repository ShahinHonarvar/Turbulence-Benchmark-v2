def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    p = 3
    while p * p <= n and n % p != 0:
        p += 2
    return p * p > n

def all_right_truncatable_prime(t):
    x = t[4]
    res = []
    for i in range(2, x):
        if is_prime(i):
            j = i
            while j != 0 and is_prime(j):
                j //= 10
            if j == 0:
                res.append(i)
    return sorted(res)