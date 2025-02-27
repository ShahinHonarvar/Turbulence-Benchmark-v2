def all_left_right_truncatable_prime(limit):
    truncatable_primes = []
    for x in range(2, limit + 1):
        if is_prime(x) and (not has_zero(x)) and is_left_right_truncatable(x):
            truncatable_primes.append(x)
    truncatable_primes.sort()
    return truncatable_primes

def is_prime(x):
    if x <= 1:
        return False
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            return False
    return True

def has_zero(x):
    return '0' in str(x)

def is_left_right_truncatable(x):
    str_x = str(x)
    for i in range(1, len(str_x)):
        left_x = int(str_x[i:])
        right_x = int(str_x[:i])
        if not is_prime(left_x) or not is_prime(right_x):
            return False
    return True