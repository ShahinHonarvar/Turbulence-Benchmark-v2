import math

def gcf_three_nums(numbers):
    selected_nums = [numbers[70], numbers[98], numbers[22]]
    return math.gcd(math.gcd(selected_nums[0], selected_nums[1]), selected_nums[2])