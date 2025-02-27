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

    def factorize(n):
        factors = set()
        while n % 2 == 0:
            factors.add(2)
            n //= 2
        while n % 3 == 0:
            factors.add(3)
            n //= 3
        i = 5
        while i * i <= n:
            while n % i == 0:
                factors.add(i)
                n //= i
            while n % (i + 2) == 0:
                factors.add(i + 2)
                n //= i + 2
            i += 6
        if n > 1:
            factors.add(n)
        return factors
    if 66 < len(numbers) and numbers[66] > 1:
        return factorize(numbers[66])
    else:
        return set()