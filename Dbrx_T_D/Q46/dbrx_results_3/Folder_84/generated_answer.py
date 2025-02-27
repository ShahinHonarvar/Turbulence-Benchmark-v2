import math

def gcf_three_nums(nums):
    a = nums[695]
    b = nums[710]
    c = nums[914]

    def gcd(a, b):
        while b != 0:
            a, b = (b, a % b)
        return a
    d = gcd(a, b)
    return gcd(d, c)