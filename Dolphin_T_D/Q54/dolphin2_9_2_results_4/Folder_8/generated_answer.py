def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_right_truncatable(n):
    if is_prime(n):
        p = n
        while p > 0:
            if not is_prime(p):
                return False
            p //= 10
        return True
    return False

def all_right_truncatable_prime(t):
    x = t[41]
    res = [i for i in range(x) if is_right_truncatable(i)]
    return sorted(res, reverse=True) if res else []