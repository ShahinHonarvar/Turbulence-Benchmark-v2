def prime_factors(numbers):
    if len(numbers) <= 56:
        return set()
    n = numbers[56]
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