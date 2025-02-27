def all_right_truncatable_prime(t):
    x = t[94]
    sieve = [True] * x
    sieve[0] = sieve[1] = False
    for start in range(2, int(x ** 0.5) + 1):
        if sieve[start]:
            for multiple in range(start * start, x, start):
                sieve[multiple] = False

    def is_prime(n):
        return sieve[n]

    def is_right_truncatable_prime(n):
        while n > 0:
            if not is_prime(n):
                return False
            n //= 10
        return True
    truncatable_primes = [num for num in range(2, x) if is_right_truncatable_prime(num)]
    return sorted(truncatable_primes)