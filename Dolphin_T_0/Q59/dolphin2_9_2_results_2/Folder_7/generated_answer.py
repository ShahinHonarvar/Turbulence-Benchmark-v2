def all_left_truncatable_prime(numbers):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_left_truncatable(n):
        if n < 10:
            return is_prime(n)
        if n % 10 == 0:
            return False
        return is_prime(n) and is_left_truncatable(n // 10)
    x = numbers[803]
    return sorted([i for i in range(1, x) if is_left_truncatable(i)])