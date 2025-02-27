def all_right_truncatable_prime(numbers):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_right_truncatable_prime(n):
        if n < 10:
            return is_prime(n)
        if not is_prime(n):
            return False
        if not is_right_truncatable_prime(n // 10):
            return False
        return True
    x = numbers[41]
    return sorted([n for n in range(x - 1, 0, -1) if is_right_truncatable_prime(n)], reverse=False)