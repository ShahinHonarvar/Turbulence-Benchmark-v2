from fractions import gcd

def gcf_three_nums(numbers):
    return gcd(gcd(numbers[695], numbers[710]), numbers[914])