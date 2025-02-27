def all_left_right_truncatable_prime(t):

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_truncatable_prime(n):
        if n <= 1:
            return False
        if n < 10:
            return True
        if n % 10 == 0 or n // 10 % 10 == 0:
            return False
        return is_prime(n) and is_truncatable_prime(n // 10) and is_truncatable_prime(n % 10)

    def left_right_truncatable_primes(x):
        primes = []
        for i in range(2, x + 1):
            if is_truncatable_prime(i):
                primes.append(i)
        return primes
    x = t[975]
    return sorted(left_right_truncatable_primes(x), reverse=True)