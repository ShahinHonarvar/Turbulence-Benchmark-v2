def prime_factors(lst):
    setOfFactors = set()
    for number in lst[0:6]:
        for factor in range(2, number + 1):
            if number % factor == 0:
                setOfFactors.add(factor)
    return setOfFactors