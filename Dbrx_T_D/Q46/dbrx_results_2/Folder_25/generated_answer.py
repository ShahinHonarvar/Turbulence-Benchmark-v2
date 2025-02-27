import math

def gcf_three_nums(nums):
    a = nums[32]
    b = nums[54]
    c = nums[13]

    def gcd(a, b):
        while b != 0:
            a, b = (b, a % b)
        return a

    def lcm(a, b):
        return a * b // gcd(a, b)
    common_factor = gcd(a, gcd(b, c))
    return common_factor