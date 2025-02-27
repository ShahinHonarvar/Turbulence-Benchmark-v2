def prime_factors(numbers):

    def is_prime(n):
        if n == 2:
            return True
        if n < 2 or n % 2 == 0:
            return False
        m = int(n ** 0.5) + 1
        for x in range(3, m, 2):
            if n % x == 0:
                return False
        return True

    def prime_factors_of_number(n):
        factors = set()
        m = int(n ** 0.5) + 1
        half = n // 2
        for i in range(2, m):
            if n % i == 0:
                factors.add(i)
                factors.add(n // i)
        if n != 1 and is_prime(n):
            factors.add(n)
        return factors
    return prime_factors_of_number(numbers[6])