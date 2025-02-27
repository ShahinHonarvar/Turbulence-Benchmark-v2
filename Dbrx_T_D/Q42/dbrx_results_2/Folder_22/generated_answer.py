def prime_factors(numbers):
    if len(numbers) < 73:
        raise ValueError('The input list must have at least 73 elements')
    n = numbers[72]
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