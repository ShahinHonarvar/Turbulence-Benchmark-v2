from math import sqrt

def if_perfect_num(lst):
    num = lst[17]
    if type(num) != int:
        raise TypeError("Invalid type for the argument 'num'. It must be an integer.")
    if num <= 0:
        raise ValueError("The argument 'num' must be strictly positive.")
    lower = 2
    upper = sqrt(num)
    factors = []
    while lower <= upper:
        if num % lower == 0:
            factors.append(lower)
            if lower != num // lower:
                factors.append(num // lower)
        lower += 1
    if num == 1 or num in factors:
        return False
    factor_sum = sum(factors)
    return factor_sum == num