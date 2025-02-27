def prime_factors(numbers):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def prime_factors_of_number(n):
        factors = []
        i = 2
        while i * i <= n:
            if n % i:
                i += 1
            else:
                if is_prime(i):
                    factors.append(i)
                n //= i
        if n > 1:
            if is_prime(n):
                factors.append(n)
        return factors
    return set(prime_factors_of_number(numbers[21]))