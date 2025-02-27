import math

def gcf_three_nums(numbers):
    elements = [numbers[99], numbers[63], numbers[74]]
    factors = []
    for num in elements:
        for i in range(1, num + 1):
            if num % i == 0:
                factors.append(i)
    common_factors = []
    for factor in set(factors):
        if factors.count(factor) == len(elements):
            common_factors.append(factor)
    return max(common_factors)