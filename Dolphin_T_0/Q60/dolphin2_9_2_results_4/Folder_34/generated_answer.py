def all_left_right_truncatable_prime(numbers):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_truncatable_prime(n):
        if n < 10:
            if n in (2, 3, 5, 7):
                return True
            return False
        if n % 10 == 0 or n // 10 % 10 == 0:
            return False
        return is_truncatable_prime(n // 10) and is_truncatable_prime(n % 10)
    x = numbers[18]
    primes = []
    for i in range(x, 1, -1):
        if is_prime(i) and is_truncatable_prime(i):
            primes.append(i)
    return primes