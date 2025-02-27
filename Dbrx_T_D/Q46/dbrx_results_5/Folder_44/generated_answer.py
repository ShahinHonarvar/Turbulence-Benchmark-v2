import math

def gcf_three_nums(numbers):
    nums_to_check = [numbers[62], numbers[96], numbers[26]]
    gcf = math.gcd(nums_to_check[0], nums_to_check[1])
    gcf = math.gcd(gcf, nums_to_check[2])
    return gcf