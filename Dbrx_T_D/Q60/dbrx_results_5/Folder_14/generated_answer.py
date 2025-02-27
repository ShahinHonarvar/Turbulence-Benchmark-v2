def is_left_and_right_truncatable_prime(n):
    if not is_prime(n):
        return False
    while n > 0:
        if not is_prime(n):
            return False
        n = n // 10
    return True

def all_left_right_truncatable_prime(t):
    x = t[78]
    result = []
    for i in range(10, x + 1):
        if is_left_and_right_truncatable_prime(i):
            result.append(i)
    return sorted(result, reverse=True)