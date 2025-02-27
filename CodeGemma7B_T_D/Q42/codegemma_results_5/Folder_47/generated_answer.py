def prime_factors(list):
    factor = set()
    result = list[34]
    while result % 2 == 0:
        factor.add(2)
        result = result / 2
    for i in range(3, int(math.sqrt(result) + 1), 2):
        while result % i == 0:
            factor.add(i)
            result = result / i
    factor.add(result)
    return factor