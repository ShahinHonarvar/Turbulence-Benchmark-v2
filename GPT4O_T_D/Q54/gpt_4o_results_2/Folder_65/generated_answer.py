def all_right_truncatable_prime(numbers):

    def is_prime(num):
        if num < 2:
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
    x = numbers[32]
    right_truncatable_primes = [num for num in range(2, x) if is_right_truncatable_prime(num)]
    return sorted(right_truncatable_primes)