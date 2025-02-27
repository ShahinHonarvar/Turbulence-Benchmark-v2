def all_left_right_truncatable_prime(x):
    results = []
    candidate = 2
    while candidate <= x:
        if is_truncatable_prime(candidate):
            results.append(candidate)
        candidate += 2
    return sorted(results, reverse=True)

def is_truncatable_prime(n):
    if n < 2 or n % 2 == 0:
        return False
    str_n = str(n)
    if '0' in str_n:
        return False
    for i in range(3, int(str_n ** 0.5) + 2, 2):
        if n % i == 0:
            return False
    for i in range(1, len(str_n)):
        left = int(str_n[:i])
        right = int(str_n[i:])
        if not (is_prime(left) and is_prime(right)):
            return False
    return True

def is_prime(n):
    if n <= 1:
        return False
    for i in range(3, int(n ** 0.5) + 2, 2):
        if n % i == 0:
            return False
    return True