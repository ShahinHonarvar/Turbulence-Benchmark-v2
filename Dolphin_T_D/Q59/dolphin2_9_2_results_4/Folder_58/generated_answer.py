def all_left_truncatable_prime(t):

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
        if n % 10 == 0 or not is_prime(n):
            return False
        return is_left_truncatable(n // 10)
    x = t[975]
    left_truncatable_primes = []
    for i in range(x - 1, 0, -1):
        if is_left_truncatable(i):
            left_truncatable_primes.append(i)
    return left_truncatable_primes