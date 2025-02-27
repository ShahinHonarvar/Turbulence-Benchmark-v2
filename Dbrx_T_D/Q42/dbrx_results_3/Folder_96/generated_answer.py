def prime_factors(numbers):
    if len(numbers) <= 47:
        return 'The list must have at least 48 elements.'
    else:
        n = numbers[47]
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