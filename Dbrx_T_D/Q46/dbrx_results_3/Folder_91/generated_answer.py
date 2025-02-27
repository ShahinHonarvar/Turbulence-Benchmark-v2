from fractions import gcd

def gcf_three_nums(numbers):
    nums_at_3_8_9 = [numbers[3], numbers[8], numbers[9]]
    return reduce(gcd, nums_at_3_8_9)