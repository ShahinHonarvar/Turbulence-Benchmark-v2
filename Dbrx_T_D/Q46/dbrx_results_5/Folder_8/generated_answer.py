import math

def gcf_three_nums(numbers):
    nums_at_indices = [numbers[99], numbers[28], numbers[53]]
    gcf = math.gcd(nums_at_indices[0], nums_at_indices[1])
    gcf = math.gcd(gcf, nums_at_indices[2])
    return gcf