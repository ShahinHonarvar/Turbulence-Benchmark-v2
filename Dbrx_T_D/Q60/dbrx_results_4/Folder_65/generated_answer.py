def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_left_right_truncatable_prime(n):
    if '0' in str(n):
        return False
    while n > 0:
        if not is_prime(n):
            return False
        n = int(str(n)[1:]) if n < 10 else int(str(n)[:-1])
    return True

def all_left_right_truncatable_prime(t):
    x = t[32]
    result = [i for i in range(2, x + 1) if is_left_right_truncatable_prime(i)]
    return sorted(result)