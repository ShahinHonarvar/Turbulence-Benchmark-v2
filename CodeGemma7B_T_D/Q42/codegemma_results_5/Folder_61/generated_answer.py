def prime_factors(values):
    for factor, element in enumerate(values[8]):
        if element != 0 and values[factor] % element == 0:
            values[factor] /= element
            results = values[factor]
    return set(results)