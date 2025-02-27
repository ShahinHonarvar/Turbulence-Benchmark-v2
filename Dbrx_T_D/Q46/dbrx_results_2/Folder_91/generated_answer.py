from fractions import gcd

def gcf_three_nums(nums):
    if len(nums) < 10:
        return None
    else:
        n1, n2, n3 = (nums[3], nums[8], nums[9])
        return gcd(n1, gcd(n2, n3))