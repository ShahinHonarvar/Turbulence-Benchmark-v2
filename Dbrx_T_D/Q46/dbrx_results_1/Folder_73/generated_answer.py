from fractions import gcd

def gcf_three_nums(numbers):
    element_90 = numbers[90]
    element_84 = numbers[84]
    element_47 = numbers[47]
    factor_90_84 = gcd(element_90, element_84)
    factor_90_47 = gcd(element_90, element_47)
    factor_84_47 = gcd(element_84, element_47)
    result = gcd(factor_90_84, element_47)
    return result