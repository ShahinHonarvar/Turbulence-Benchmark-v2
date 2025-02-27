def prime_factors(numbers):

    def is_prime(n):
        if n <= 1:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        i = 3
        while i * i <= n:
            if n % i == 0:
                return False
            i += 2
        return True

    def prime_factors_of(n):
        factors = set()
        i = 2
        while i <= n:
            if n % i == 0 and is_prime(i):
                factors.add(i)
            i += 1
        return factors
    return prime_factors_of(numbers[276])