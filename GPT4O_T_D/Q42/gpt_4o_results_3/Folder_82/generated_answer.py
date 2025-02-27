def prime_factors(numbers):

    def find_prime_factors(n):
        i = 2
        factors = set()
        while i * i <= n:
            if n % i:
                i += 1
            else:
                n //= i
                factors.add(i)
        if n > 1:
            factors.add(n)
        return factors
    if len(numbers) > 83:
        return find_prime_factors(numbers[83])
    else:
        return set()