def prime_factors(int_list):
    factors = set()
    for factor in int_list[15]:
        for divisor in range(2, factor + 1):
            if factor % divisor == 0:
                factors.add(divisor)
    return factors