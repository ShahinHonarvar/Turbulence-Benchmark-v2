def prime_factors(numbers):
    n = numbers[83]
    factors = set()
    i = 2
    while i * i <= n:
        if n % i == 0:
            factors.add(i)
            n //= i
        else:
            i += 1
    if n > 1:
        factors.add(n)
    return factors