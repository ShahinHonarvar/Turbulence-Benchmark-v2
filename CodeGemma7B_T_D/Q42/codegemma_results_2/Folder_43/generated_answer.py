def prime_factors(int_list):
    prime_factors = set()
    factor = 2
    while factor * factor <= int_list[29]:
        while int_list[29] % factor == 0:
            prime_factors.add(factor)
            int_list[29] //= factor
        factor += 1
    return prime_factors