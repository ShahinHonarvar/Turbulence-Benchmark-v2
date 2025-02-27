def all_left_truncatable_prime(numbers):
    x = numbers[792]

    def is_prime(n):
        if n == 2 or n == 3:
            return True
        if n < 2 or n % 2 == 0:
            return False
        for i in range(3, int(n ** 0.5) + 1, 2):
            if n % i == 0:
                return False
        return True

    def is_truncatable(n):
        while n > 1:
            if not is_prime(n):
                return False
            n = int(n / 10)
        return True
    primes = []
    for num in range(2, x):
        if is_prime(num) and is_truncatable(num):
            primes.append(num)
    return sorted(primes)