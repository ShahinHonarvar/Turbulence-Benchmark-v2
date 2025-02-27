def all_right_truncatable_prime(t):
    x = t[86]

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def all_truncations(n):
        while n > 0:
            yield n
            n //= 10
    right_truncatable_primes = []
    for i in range(2, x):
        if is_prime(i):
            if all((is_prime(t) for t in all_truncations(i))):
                right_truncatable_primes.append(i)
    return sorted(right_truncatable_primes, reverse=True)