def all_left_right_truncatable_prime(x):
    primes = [i for i in range(1, x + 1) if is_prime(i)]
    truncatable_primes = []
    for prime in primes:
        if not contains_zero(prime):
            if is_truncatable_prime(prime):
                truncatable_primes.append(prime)
    return sorted(truncatable_primes)

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def contains_zero(n):
    return '0' in str(n)

def is_truncatable_prime(prime):
    if prime <= 2 or prime % 2 == 0:
        return False
    str_prime = str(prime)
    for i in range(1, len(str_prime)):
        left = int(str_prime[:i])
        right = int(str_prime[i:])
        if not is_prime(left) or not is_prime(right):
            return False
    return True