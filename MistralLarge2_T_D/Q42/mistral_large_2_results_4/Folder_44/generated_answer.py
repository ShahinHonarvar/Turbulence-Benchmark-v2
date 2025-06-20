def prime_factors(numbers):

    def factors(n):
        i = 2
        factors_set = set()
        while i * i <= n:
            if n % i:
                i += 1
            else:
                n //= i
                factors_set.add(i)
        if n > 1:
            factors_set.add(n)
        return factors_set
    if len(numbers) > 828:
        return factors(numbers[828])
    else:
        return set()