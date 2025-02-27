def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_right_truncatable_prime(n):
    while n > 10:
        if not is_prime(n):
            return False
        n //= 10
    return is_prime(n)

def all_right_truncatable_prime(t):
    x = t[50]
    res = [i for i in range(x - 1, 0, -1) if is_right_truncatable_prime(i)]
    return sorted(res, reverse=True) or []