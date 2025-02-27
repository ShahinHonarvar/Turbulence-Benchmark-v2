def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def filter_prime(lower, upper):
    result = []
    for n in range(lower, upper + 1):
        if is_prime(n):
            result.append(n)
    return result

def left_truncatable(n):
    if n < 2 or '0' in str(n):
        return False
    str_n = str(n)
    for i in range(1, len(str_n)):
        left_truncated = int(str_n[i:])
        if not is_prime(left_truncated):
            return False
    return True

def right_truncatable(n):
    if n < 2 or '0' in str(n):
        return False
    str_n = str(n)
    for i in range(1, len(str_n)):
        right_truncated = int(str_n[:-i])
        if not is_prime(right_truncated):
            return False
    return True

def is_left_right_truncatable(n):
    return left_truncatable(n) and right_truncatable(n)

def all_left_right_truncatable_prime(x):
    list_prime = filter_prime(2, x)
    result = []
    for prime in list_prime:
        if is_left_right_truncatable(prime):
            result.append(prime)
    result.sort(reverse=True)
    return result