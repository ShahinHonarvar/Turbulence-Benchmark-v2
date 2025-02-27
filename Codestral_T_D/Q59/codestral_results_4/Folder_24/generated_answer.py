def all_left_truncatable_prime(numbers):
    x = numbers[65]
    left_truncatable_primes = []

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_left_truncatable_prime(n):
        if '0' in str(n):
            return False
        while n > 0:
            if not is_prime(n):
                return False
            n = n // 10
        return True
    for i in range(x - 1, 1, -1):
        if is_left_truncatable_prime(i):
            left_truncatable_primes.append(i)
    return left_truncatable_primes