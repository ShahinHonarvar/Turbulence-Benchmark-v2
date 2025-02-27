def all_right_truncatable_prime(t):
    x = t[835]
    res = []
    for n in range(1, x):
        if is_prime(n) and is_right_truncatable_prime(n):
            res.append(n)
    return sorted(res)

def is_prime(n):
    if n == 2 or n == 3:
        return True
    if n % 2 == 0 or n == 1:
        return False
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True

def is_right_truncatable_prime(n):
    while n != 0:
        if not is_prime(n):
            return False
        n //= 10
    return True