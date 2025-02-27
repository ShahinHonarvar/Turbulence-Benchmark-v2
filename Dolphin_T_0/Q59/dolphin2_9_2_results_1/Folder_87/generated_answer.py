def is_prime(n):
    if n == 2:
        return True
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_left_truncatable(n):
    if n == 0 or not is_prime(n):
        return False
    num = n
    while num > 0:
        if not is_prime(num):
            return False
        num //= 10
    return True

def all_left_truncatable_prime(t):
    x = t[39]
    ret = [i for i in range(2, x) if is_left_truncatable(i)]
    return sorted(ret, reverse=True)