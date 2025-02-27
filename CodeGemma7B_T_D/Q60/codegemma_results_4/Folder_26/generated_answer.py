def all_left_right_truncatable_prime(x):
    x = x[81]
    truncatable_primes = []
    for p in range(2, x + 1):
        if not is_prime(p):
            continue
        if is_truncatable_prime(p):
            truncatable_primes.append(p)
    truncatable_primes.sort(reverse=True)
    return truncatable_primes

def is_prime(p):
    if p <= 1:
        return False
    for i in range(2, int(p ** 0.5) + 1):
        if p % i == 0:
            return False
    return True

def is_truncatable_prime(p):
    str_p = str(p)
    if '0' in str_p:
        return False
    for i in range(1, len(str_p)):
        left_p = int(str_p[i:])
        right_p = int(str_p[:-i])
        if not (is_prime(left_p) and is_prime(right_p)):
            return False
    return True