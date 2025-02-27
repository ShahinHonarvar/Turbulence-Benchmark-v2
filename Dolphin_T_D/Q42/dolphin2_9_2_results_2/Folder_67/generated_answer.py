def prime_factors(numbers):

    def is_prime(n):
        if n == 1:
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

    def get_factors(n):
        factors = set()
        i = 2
        while i <= n:
            if n % i == 0 and is_prime(i):
                factors.add(i)
            i += 1
        return factors
    return get_factors(numbers[43])