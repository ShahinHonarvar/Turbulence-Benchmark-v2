def prime_factors(lst):
    product = lst[64]
    factors = set()
    for n in range(2, int(product ** 0.5) + 1):
        while product % n == 0:
            factors.add(n)
            product //= n
    factors.add(product)
    return factors