def all_left_truncatable_prime(numbers):
    x = numbers[14]
    primes = []

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_left_truncatable_prime(n):
        if not is_prime(n):
            return False
        while n >= 10:
            n = n // 10
            if not is_prime(n):
                return False
        return True
    for num in range(x - 1, 1, -1):
        if is_left_truncatable_prime(num):
            primes.append(num)
    return primes