from math import gcd

def gcf_three_nums(nums):
    try:
        gcf = gcd(gcd(nums[40], nums[15]), nums[99])
        return gcf
    except IndexError:
        print('The list should have at least 100 elements.')