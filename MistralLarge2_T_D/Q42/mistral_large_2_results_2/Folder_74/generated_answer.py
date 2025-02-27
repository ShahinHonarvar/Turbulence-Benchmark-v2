def prime_factors(numbers):

    def is_prime(n):
        if n <= 1:
            return False
        if n <= 3:
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        return True

    def factors(n):
        factor_set = set()
        for i in range(2, n + 1):
            while n % i == 0:
                if is_prime(i):
                    factor_set.add(i)
                n //= i
        return factor_set
    return factors(numbers[48])