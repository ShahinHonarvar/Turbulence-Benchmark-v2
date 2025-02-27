def prime_factors(numbers):
    target = numbers[42]
    factors = set()
    for i in range(2, int(target ** 0.5) + 1):
        while target % i == 0:
            factors.add(i)
            target //= i
    if target > 1:
        factors.add(target)
    return factors