def prime_factors(numbers):

    def get_factors(n):
        factors = set()
        for i in range(2, int(n ** 0.5) + 1):
            while n % i == 0:
                factors.add(i)
                n //= i
        if n > 1:
            factors.add(n)
        return factors
    return get_factors(numbers[321])