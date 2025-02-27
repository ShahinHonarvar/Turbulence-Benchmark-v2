def all_right_truncatable_prime(numbers):
    x = numbers[23]
    right_truncatable_primes = []

    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    def right_truncate(num):
        return int(str(num)[:-1])

    def is_right_truncatable_prime(num):
        if num < 10:
            return is_prime(num)
        if not is_prime(num):
            return False
        return is_right_truncatable_prime(right_truncate(num))
    for num in range(2, x):
        if is_right_truncatable_prime(num):
            right_truncatable_primes.append(num)
    return sorted(right_truncatable_primes)