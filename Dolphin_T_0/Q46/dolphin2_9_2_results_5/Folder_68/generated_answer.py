from math import gcd as GCD

def gcf_three_nums(nums_list):
    return GCD(nums_list[4], GCD(nums_list[1], nums_list[7]))