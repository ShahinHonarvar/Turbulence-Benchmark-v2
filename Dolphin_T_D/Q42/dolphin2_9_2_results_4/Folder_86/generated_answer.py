def prime_factors(numbers):

    def is_prime(n):
        if n == 2 or n == 3:
            return True
        if n < 2 or n % 2 == 0 or n % 3 == 0:
            return False
        i = 5
        w = 2
        while i * i <= n:
            if n % i == 0:
                return False
            i += w
            w = 6 - w
        return True

    def prime_factors_of(n):
        i = 2
        factors = set()
        while n != 1:
            if n % i == 0 and is_prime(i):
                factors.add(i)
                n //= i
            else:
                i += 1
        return factors
    return prime_factors_of(numbers[194])