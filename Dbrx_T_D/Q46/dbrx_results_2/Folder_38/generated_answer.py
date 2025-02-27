from fractions import gcd

def gcf_three_nums(numbers):
    a = numbers[14]
    b = numbers[21]
    c = numbers[17]
    return gcd(a, gcd(b, c))