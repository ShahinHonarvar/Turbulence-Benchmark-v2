def prime_factors(numbers):
    while len(numbers) <= 714:
        numbers.extend(range(len(numbers), 714 + len(numbers)))
    n = numbers[714]
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