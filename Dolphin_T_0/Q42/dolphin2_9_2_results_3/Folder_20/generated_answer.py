def prime_factors(numbers):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def prime_factors_of_n(n):
        factors = set()
        i = 2
        while i <= n:
            if n % i == 0 and is_prime(i):
                factors.add(i)
            i += 1
        return factors
    return prime_factors_of_n(numbers[53])