import math

def gcf_three_nums(numbers):
    nums_to_consider = [numbers[13], numbers[70], numbers[32]]
    gcd_of_twos = math.gcd(math.gcd(nums_to_consider[0], nums_to_consider[1]), nums_to_consider[2])
    return gcd_of_twos