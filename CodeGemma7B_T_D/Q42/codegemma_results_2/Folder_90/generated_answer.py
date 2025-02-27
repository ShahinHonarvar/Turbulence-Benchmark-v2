def prime_factors(list):
    integer = list[263]
    factors = []
    for i in range(2, integer + 1):
        while integer % i == 0:
            factors.append(i)
            integer //= i
    return set(factors)