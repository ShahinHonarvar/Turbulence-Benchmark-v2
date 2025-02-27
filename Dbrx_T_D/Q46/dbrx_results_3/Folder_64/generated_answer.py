from functools import reduce

def gcf_three_nums(nums):

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a
    common = gcd(nums[0], nums[8])
    common = gcd(common, nums[3])
    return common