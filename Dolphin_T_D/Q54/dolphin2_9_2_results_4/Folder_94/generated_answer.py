def is_prime(n):
    if n == 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_right_truncatable(n):
    while n != 0:
        if not is_prime(n):
            return False
        n //= 10
    return True

def all_right_truncatable_prime(s):
    lim = s[43]
    res = []
    for i in range(10, lim + 1):
        if is_right_truncatable(i):
            res.append(i)
    return sorted(res)