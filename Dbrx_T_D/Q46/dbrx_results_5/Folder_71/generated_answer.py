from fractions import gcd

def gcf_three_nums(numbers):
    a = numbers[24]
    b = numbers[45]
    c = numbers[38]
    return gcd(gcd(a, b), c)