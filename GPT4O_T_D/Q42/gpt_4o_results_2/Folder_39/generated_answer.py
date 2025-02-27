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
        if n % 2 == 0:
            factors.add(2)
            while n % 2 == 0:
                n //= 2
        for i in range(3, int(n ** 0.5) + 1, 2):
            if n % i == 0 and is_prime(i):
                factors.add(i)
                while n % i == 0:
                    n //= i
        if n > 2 and is_prime(n):
            factors.add(n)
        return factors
    if len(numbers) > 59:
        return factorize(numbers[59])
    return set()