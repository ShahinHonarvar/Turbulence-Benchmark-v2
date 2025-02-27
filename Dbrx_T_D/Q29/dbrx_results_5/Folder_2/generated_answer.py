from functools import reduce

def gcf_two_nums(nums):

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a
    a, b = (nums[372], nums[752])
    return reduce(gcd, filter(lambda x: x > 0, (a, b)))