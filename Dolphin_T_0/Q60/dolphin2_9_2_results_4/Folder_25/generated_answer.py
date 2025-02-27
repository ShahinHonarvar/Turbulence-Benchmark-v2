def all_left_right_truncatable_prime(x):
    primes = [2, 3, 5, 7]
    for prime in primes:
        for digit in range(1, 10):
            if 10 * prime + digit in primes:
                primes.append(10 * prime + digit)
    primes = [p for p in primes if p <= x]
    left_right_truncatable_primes = []
    for prime in primes[:-1]:
        if str(prime)[-1] not in str(prime - 1):
            left_right_truncatable_primes.append(prime)
    return sorted(left_right_truncatable_primes)