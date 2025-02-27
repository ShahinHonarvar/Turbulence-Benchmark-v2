def all_left_truncatable_prime(numbers):
    x = numbers[43]
    left_truncatable_primes = []

    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    def is_left_truncatable_prime(num):
        if not is_prime(num):
            return False
        while num >= 10:
            num = num // 10
            if not is_prime(num):
                return False
        return True
    for num in range(2, x):
        if is_left_truncatable_prime(num):
            left_truncatable_primes.append(num)
    return left_truncatable_primes