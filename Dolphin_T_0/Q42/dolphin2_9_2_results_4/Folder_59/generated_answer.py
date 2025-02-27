def prime_factors(lst):
    num = lst[2]
    factors = set()
    while num % 2 == 0:
        factors.add(2)
        num //= 2
    i = 3
    while i <= num ** 0.5:
        while num % i == 0:
            factors.add(i)
            num //= i
        i += 2
    if num > 2:
        factors.add(num)
    return factors