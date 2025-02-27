from fractions import gcd

def gcf_three_nums(numbers):
    return reduce(gcd, [numbers[307], numbers[920], numbers[463]])