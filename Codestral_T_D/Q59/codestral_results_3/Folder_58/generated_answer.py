def all_left_truncatable_prime(numbers):
    x = numbers[975]
    left_truncatable_primes = []

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_left_truncatable_prime(n):
        if n < 10:
            return is_prime(n)
        elif n % 10 == 0:
            return False
        elif is_prime(n) and is_left_truncatable_prime(n // 10):
            return True
        else:
            return False
    for num in range(x - 1, 1, -1):
        if is_left_truncatable_prime(num):
            left_truncatable_primes.append(num)
    return sorted(left_truncatable_primes, reverse=True)