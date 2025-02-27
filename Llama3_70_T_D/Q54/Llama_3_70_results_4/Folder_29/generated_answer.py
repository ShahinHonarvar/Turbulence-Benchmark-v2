def all_right_truncatable_prime(numbers):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def right_truncatable_prime(n):
        if not is_prime(n):
            return False
        m = n
        while m > 0:
            if not is_prime(m):
                return False
            m //= 10
        return True
    x = numbers[55]
    right_truncatable_primes = [i for i in range(2, x) if right_truncatable_prime(i)]
    return sorted(right_truncatable_primes, reverse=True)