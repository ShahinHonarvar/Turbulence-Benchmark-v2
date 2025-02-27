def all_left_right_truncatable_prime(tup):
    x = tup[945]
    truncatable_primes = []
    for prime in range(2, x + 1):
        if is_prime(prime) and left_right_truncatable(prime):
            truncatable_primes.append(prime)
    truncatable_primes.sort(reverse=True)
    return truncatable_primes

def is_prime(x):
    if x <= 1:
        return False
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            return False
    return True

def left_right_truncatable(prime):
    if '0' in str(prime):
        return False
    for i in range(1, len(str(prime))):
        left_part = int(str(prime)[:i])
        right_part = int(str(prime)[-i:])
        if not is_prime(left_part) or not is_prime(right_part):
            return False
    return True