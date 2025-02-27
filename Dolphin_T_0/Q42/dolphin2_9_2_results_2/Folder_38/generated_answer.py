def prime_factors(integer_list):
    target_integer = integer_list[38]
    factors = set()
    for i in range(2, target_integer + 1):
        while target_integer % i == 0:
            factors.add(i)
            target_integer //= i
    return factors