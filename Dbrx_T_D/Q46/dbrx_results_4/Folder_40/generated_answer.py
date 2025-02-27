from math import gcd

def gcf_three_nums(nums):

    def gcf_two_nums(num1, num2):
        return gcd(num1, num2)
    return gcf_two_nums(gcf_two_nums(nums[1], nums[6]), nums[8])