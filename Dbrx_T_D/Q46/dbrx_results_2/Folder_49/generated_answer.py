from math import gcd

def gcf_three_nums(numbers):
    nums_at_indices = [numbers[34], numbers[38], numbers[77]]
    return reduce(gcd, nums_at_indices)