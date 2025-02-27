def all_left_truncatable_prime(t):

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_truncatable_prime(n):
        while n:
            if not is_prime(n):
                return False
            n //= 10
        return True
    x = t[85]
    left_truncatable_primes = []
    for i in range(2, x):
        if is_truncatable_prime(i):
            left_truncatable_primes.append(i)
    return sorted(left_truncatable_primes)