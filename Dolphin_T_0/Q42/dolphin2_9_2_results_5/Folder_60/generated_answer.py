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
            if n % i:
                i += 2
            else:
                return False
        return True

    def prime_factors_of(n):
        factors = set()
        i = 2
        while i * i <= n:
            if n % i:
                i += 1
            else:
                if is_prime(i):
                    factors.add(i)
                n //= i
        if n > 1 and is_prime(n):
            factors.add(n)
        return factors
    return prime_factors_of(numbers[88])