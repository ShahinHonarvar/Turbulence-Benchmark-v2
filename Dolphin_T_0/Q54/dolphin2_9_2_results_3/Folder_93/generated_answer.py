def all_right_truncatable_prime(x):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    primes = []
    for i in range(2, x):
        if is_prime(i):
            primes.append(i)
    right_truncatable_primes = []
    for prime in primes:
        while prime > 0 and is_prime(prime):
            right_truncatable_primes.append(prime)
            prime //= 10
    return sorted(right_truncatable_primes)