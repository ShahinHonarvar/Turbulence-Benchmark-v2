def all_left_truncatable_prime(x):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_left_truncatable(n):
        if n == 0:
            return True
        if n % 10 == 0:
            return False
        return is_prime(n) and is_left_truncatable(n // 10)
    primes = []
    for i in range(x - 1, 1, -1):
        if is_left_truncatable(i):
            primes.append(i)
    return primes