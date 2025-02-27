def all_left_truncatable_prime(numbers):
    x = numbers[835]
    primes = []

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
        if n % 10 == 0:
            return False
        return is_prime(n) and is_left_truncatable_prime(n // 10)
    for num in range(2, x):
        if is_left_truncatable_prime(num):
            primes.append(num)
    return sorted(primes)