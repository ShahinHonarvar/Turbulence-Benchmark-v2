def prime_factors(numbers):

    def is_prime(n):
        if n <= 1:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        sqrt_n = int(n ** 0.5) + 1
        for i in range(3, sqrt_n, 2):
            if n % i == 0:
                return False
        return True
    n = numbers[10]
    factors = set()
    for i in range(2, n + 1):
        while n % i == 0 and is_prime(i):
            factors.add(i)
            n = n / i
    return factors