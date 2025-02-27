import math

def prime_factors(integer_list):
    factor_set = set()
    number = integer_list[72]
    while number % 2 == 0:
        factor_set.add(2)
        number = number // 2
    for i in range(3, int(math.sqrt(number)) + 1, 2):
        while number % i == 0:
            factor_set.add(i)
            number = number // i
    if number > 2:
        factor_set.add(number)
    return factor_set