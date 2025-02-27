def is_prime(n):
    if n < 2:
        return False
    factors = range(2, int(n ** 0.5) + 1)
    for factor in factors:
        if n % factor == 0:
            return False
    return True

def all_left_right_truncatable_prime(x):
    primes = [i for i in range(x, 0, -1) if is_prime(i)]
    left_right_truncatable_primes = []
    for prime in primes:
        if all(('0' not in str(prime - i - j) for i in range(len(str(prime))) for j in (0, 1))):
            left_right_truncatable_primes.append(prime)
    return sorted(left_right_truncatable_primes)