def prime_factors(numbers):
    target = numbers[51]
    factors = set()
    for i in range(2, int(target ** 0.5) + 1):
        if target % i == 0:
            factors.add(i)
            while target % i == 0:
                target //= i
    if target > 1:
        factors.add(target)
    return factors