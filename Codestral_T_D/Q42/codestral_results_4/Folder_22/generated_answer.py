def prime_factors(numbers):
    target = numbers[72]
    factors = set()
    i = 2
    while i * i <= target:
        if target % i:
            i += 1
        else:
            target //= i
            factors.add(i)
    if target > 1:
        factors.add(target)
    return factors