def prime_factors(integer_list):
    if len(integer_list) < 223:
        raise ValueError('The list does not have an index 222')
    target_integer = integer_list[222]
    i = 2
    factors = set()
    while i * i <= target_integer:
        if target_integer % i:
            i += 1
        else:
            target_integer //= i
            factors.add(i)
    if target_integer > 1:
        factors.add(target_integer)
    return factors