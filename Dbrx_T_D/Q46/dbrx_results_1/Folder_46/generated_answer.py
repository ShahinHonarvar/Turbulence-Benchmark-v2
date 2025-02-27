import math

def gcf_three_nums(numbers):
    nums_to_consider = [numbers[78], numbers[19], numbers[13]]
    gcd_of_two = math.gcd(nums_to_consider[0], nums_to_consider[1])
    gcf = math.gcd(gcd_of_two, nums_to_consider[2])
    return gcf