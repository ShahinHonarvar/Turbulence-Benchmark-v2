import math

def gcf_three_nums(nums):
    a = nums[27]
    b = nums[85]
    c = nums[51]

    def gcd(a, b):
        while b != 0:
            a, b = (b, a % b)
        return abs(a)
    g1 = gcd(a, b)
    g2 = gcd(g1, c)
    return g2