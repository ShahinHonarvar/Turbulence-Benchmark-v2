def all_right_truncatable_prime(numbers):
    x = numbers[79]

    def is_prime(num):
        if num <= 1:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    def is_right_truncatable_prime(num):
        while num > 0:
            if not is_prime(num):
                return False
            num //= 10
        return True
    return sorted(filter(is_right_truncatable_prime, range(2, x)), reverse=True)