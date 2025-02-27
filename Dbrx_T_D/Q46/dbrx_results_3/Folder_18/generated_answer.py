import math

def gcf_three_nums(nums):
    a, b, c = (nums[637], nums[411], nums[757])

    def gcd(a, b):
        while b != 0:
            a, b = (b, a % b)
        return a
    hcf = gcd(a, b)
    return math.gcd(c, hcf)