def prime_factors(numbers):
    target = numbers[53]
    factors = set()
    i = 2
    while i * i <= target:
        if target % i == 0:
            factors.add(i)
            target //= i
        else:
            i += 1
    if target > 1:
        factors.add(target)
    return factors