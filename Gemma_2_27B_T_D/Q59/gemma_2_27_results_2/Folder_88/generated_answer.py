def all_left_truncatable_prime(numbers):
    x = numbers[93]

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_left_truncatable_prime(num):
        if '0' in str(num):
            return False
        while num > 0:
            if not is_prime(num):
                return False
            num //= 10
        return True
    return sorted([num for num in range(2, x) if is_left_truncatable_prime(num)])