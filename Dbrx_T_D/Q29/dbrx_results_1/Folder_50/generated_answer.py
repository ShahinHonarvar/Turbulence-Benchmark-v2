import functools

def gcf_two_nums(nums):

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a
    num1, num2 = (nums[90], nums[54])
    return functools.reduce(gcd, [num1, num2])