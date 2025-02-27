def all_right_truncatable_prime(x):

    def is_prime(n):
        if n <= 1:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        for i in range(3, int(n ** 0.5) + 1, 2):
            if n % i == 0:
                return False
        return True

    def is_right_truncatable_prime(n):
        for i in range(n, 0, -1):
            if not is_prime(i):
                return False
        return True
    primes = [i for i in range(2, x) if is_prime(i)]
    right_truncatable_primes = [i for i in primes if is_right_truncatable_prime(i)]
    return sorted(right_truncatable_primes)