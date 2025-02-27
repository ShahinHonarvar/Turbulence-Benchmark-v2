def all_left_truncatable_prime(numbers):
    x = numbers[55]

    def is_prime(n):
        if n in (0, 1):
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_left_truncatable_prime(n):
        m = n
        while m:
            if not is_prime(m):
                return False
            m //= 10
        return True
    return [n for n in range(2, x) if is_left_truncatable_prime(n)]