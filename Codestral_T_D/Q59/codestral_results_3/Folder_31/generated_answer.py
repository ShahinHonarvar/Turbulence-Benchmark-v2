def all_left_truncatable_prime(t):
    x = t[50]
    primes = []

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_left_truncatable_prime(n):
        while n > 0:
            if not is_prime(n):
                return False
            n //= 10
        return True
    for i in range(2, x):
        if '0' not in str(i) and is_left_truncatable_prime(i):
            primes.append(i)
    return sorted(primes, reverse=True)