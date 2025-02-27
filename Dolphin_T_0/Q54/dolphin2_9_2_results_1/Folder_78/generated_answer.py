def all_right_truncatable_prime(num_tuple):

    def is_prime(n):
        if n == 2 or n == 3:
            return True
        if n < 2 or n % 2 == 0:
            return False
        for i in range(3, int(n ** 0.5) + 1, 2):
            if n % i == 0:
                return False
        return True

    def is_right_truncatable(n):
        if n < 10:
            return is_prime(n)
        return is_prime(n) and is_right_truncatable(n // 10)
    x = num_tuple[23]
    primes = [i for i in range(2, x) if is_prime(i) and is_right_truncatable(i)]
    return sorted(primes)