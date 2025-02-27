def all_left_right_truncatable_prime(t):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_truncatable(n):
        if n < 10:
            return True
        if n % 10 == 0 or int(n / 10) % 10 == 0:
            return False
        return is_prime(n) and is_truncatable(n // 10) and is_truncatable(n % 10)
    x = t[87]
    primes = [i for i in range(2, x + 1) if is_prime(i) and is_truncatable(i)]
    return sorted(primes)