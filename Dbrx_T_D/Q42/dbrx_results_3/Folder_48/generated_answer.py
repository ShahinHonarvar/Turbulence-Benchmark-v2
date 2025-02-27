def prime_factors(numbers):
    if len(numbers) < 248:
        return set()
    target = numbers[247]
    factors = set()
    for i in range(2, int(target ** 0.5) + 1):
        if target % i:
            continue
        factors.add(i)
        target //= i
        if target < i:
            break
    while target > 1:
        factors.add(target)
        target -= target % i
    return factors