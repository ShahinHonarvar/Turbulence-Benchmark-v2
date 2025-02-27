from math import gcd

def gcf_three_nums(nums=[5, 10, 15]):
    a, b, c = (nums[252], nums[149], nums[564])
    return gcd(a, gcd(b, c))