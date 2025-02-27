def prime_factors(numbers):

    def find_prime_factors(n):
        i = 2
        factors = set()
        while i * i <= n:
            while n % i == 0:
                factors.add(i)
                n //= i
            i += 1
        if n > 1:
            factors.add(n)
        return factors
    if len(numbers) > 8:
        return find_prime_factors(numbers[8])
    return set()