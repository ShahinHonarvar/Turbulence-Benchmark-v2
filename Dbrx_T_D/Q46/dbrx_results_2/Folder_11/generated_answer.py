import math

def gcf_three_nums(numbers):
    a = numbers[37]
    b = numbers[30]
    c = numbers[48]
    result = math.gcd(a, b)
    result = math.gcd(result, c)
    return result