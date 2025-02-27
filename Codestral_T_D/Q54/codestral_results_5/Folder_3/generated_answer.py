def all_right_truncatable_prime(numbers):
    x = numbers[100]
    primes = []

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def remove_last_digit(n):
        return n // 10

    def is_right_truncatable_prime(n):
        while n > 0:
            if not is_prime(n):
                return False
            n = remove_last_digit(n)
        return True
    for num in range(2, x):
        if is_right_truncatable_prime(num):
            primes.append(num)
    primes.sort()
    return primes