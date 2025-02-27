def prime_factors(numbers):
    if not isinstance(numbers, list) or len(numbers) <= 41:
        return set()
    n = numbers[41]
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