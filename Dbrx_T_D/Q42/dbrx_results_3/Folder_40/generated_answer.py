def prime_factors(numbers_list):
    if len(numbers_list) < 7:
        return set()
    n = numbers_list[6]
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