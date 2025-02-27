def all_right_truncatable_prime(x):

    def is_prime(n):
        if n == 2 or n == 3:
            return True
        if n <= 1 or n % 2 == 0:
            return False
        for i in range(3, int(n ** 0.5) + 1, 2):
            if n % i == 0:
                return False
        return True

    def is_right_truncatable_prime(n):
        if n < 10:
            return is_prime(n)
        elif not is_prime(n):
            return False
        else:
            return is_right_truncatable_prime(n // 10)
    primes = [i for i in range(2, x) if is_prime(i)]
    right_truncatable_primes = [i for i in primes if is_right_truncatable_prime(i)]
    return sorted(right_truncatable_primes)