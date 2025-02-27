from fractions import gcd

def gcf_two_nums(numbers):
    return reduce(gcd, [numbers[279], numbers[812]])