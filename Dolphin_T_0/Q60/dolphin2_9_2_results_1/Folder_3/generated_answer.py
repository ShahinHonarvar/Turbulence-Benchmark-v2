def all_left_right_truncatable_prime(numbers):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_truncatable_prime(n):
        if n < 10:
            return is_prime(n)
        if n % 10 == 0:
            return False
        while n > 9:
            n = n // 10
            if not is_prime(n):
                return False
        return is_prime(n)
    x = numbers[100]
    return sorted([i for i in range(x + 1) if is_truncatable_prime(i) and is_prime(i)])