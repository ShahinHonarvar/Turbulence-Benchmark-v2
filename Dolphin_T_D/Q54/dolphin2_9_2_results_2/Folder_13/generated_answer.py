def all_right_truncatable_prime(x):

    def is_prime(n):
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_truncatable_prime(n):
        while n > 10:
            if not is_prime(n):
                return False
            n = int(n / 10)
        return is_prime(n)
    primes = []
    for i in range(2, x):
        if is_truncatable_prime(i):
            primes.append(i)
    return sorted(primes)