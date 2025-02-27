def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def is_right_truncatable(p):
    if not is_prime(p):
        return False
    right = p
    while right > 0:
        if not is_prime(right):
            return False
        right //= 10
    return True

def all_right_truncatable_prime(t):
    x = t[4]
    res = [i for i in range(2, x) if is_right_truncatable(i)]
    return sorted(res) if res else []