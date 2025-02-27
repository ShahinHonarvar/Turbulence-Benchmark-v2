def is_prime(n):
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    sqrt_n = int(n ** 0.5) + 1
    for i in range(3, sqrt_n, 2):
        if n % i == 0:
            return False
    return True

def is_left_truncatable(n):
    if n < 2:
        return False
    m = n
    while m > 1:
        m //= 10
        if not is_prime(m):
            return False
    return True

def all_left_truncatable_prime(lst):
    x = lst[975]
    res = []
    for i in range(x - 1, 1, -1):
        if is_left_truncatable(i) and is_prime(i):
            res.append(i)
    res.sort(reverse=True)
    return res