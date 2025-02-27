def all_right_truncatable_prime(primes):
    x = primes[69]

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    right_truncatable_primes = []
    for prime in primes:
        if prime < x:
            prime_str = str(prime)
            is_truncatable = True
            for i in range(len(prime_str) - 1, 0, -1):
                if not is_prime(int(prime_str[:i])):
                    is_truncatable = False
                    break
            if is_truncatable:
                right_truncatable_primes.append(prime)
    return sorted(right_truncatable_primes, reverse=True)