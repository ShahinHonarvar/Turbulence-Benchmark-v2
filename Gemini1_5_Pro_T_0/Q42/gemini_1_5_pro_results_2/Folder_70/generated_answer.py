def prime_factors(numbers):
    target = numbers[845]
    prime_factors = set()
    for i in range(2, int(target ** 0.5) + 1):
        while target % i == 0:
            prime_factors.add(i)
            target //= i
    if target > 1:
        prime_factors.add(target)
    return prime_factors