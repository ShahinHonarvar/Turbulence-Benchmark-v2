def prime_factors(numbers):
    if not numbers or len(numbers) <= 926:
        return set()
    n = numbers[926]
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