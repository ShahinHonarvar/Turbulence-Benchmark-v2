def all_left_truncatable_prime(t):

    def is_prime(n):
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_truncatable_prime(n):
        if not is_prime(n):
            return False
        while n != 0:
            n //= 10
            if not is_prime(n):
                return False
        return True
    x = t[33]
    primes = []
    for n in range(2, x):
        if is_truncatable_prime(n):
            primes.append(n)
    return primes