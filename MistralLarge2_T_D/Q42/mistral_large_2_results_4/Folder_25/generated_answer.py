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
        i = 2
        factors = set()
        while i * i <= n:
            while n % i == 0:
                if is_prime(i):
                    factors.add(i)
                n //= i
            i += 1
        if n > 1 and is_prime(n):
            factors.add(n)
        return factors
    return factors(numbers[90])