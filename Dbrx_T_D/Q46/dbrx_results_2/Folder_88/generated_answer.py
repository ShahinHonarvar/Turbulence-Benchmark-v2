import math

def gcf_three_nums(numbers):
    nums_to_consider = [numbers[47], numbers[10], numbers[28]]
    gcf = math.gcd(nums_to_consider[0], nums_to_consider[1])
    gcf = math.gcd(gcf, nums_to_consider[2])
    return gcf