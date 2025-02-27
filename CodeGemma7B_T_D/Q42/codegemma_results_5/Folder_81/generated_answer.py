def prime_factors(lst):
    factor = set()
    for number in lst[20]:
        for divisor in range(2, number):
            if number % divisor == 0:
                factor.add(divisor)
        if number > 1:
            factor.add(number)
    return factor