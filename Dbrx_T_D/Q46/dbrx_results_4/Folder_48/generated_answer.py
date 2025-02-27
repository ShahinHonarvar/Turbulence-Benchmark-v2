import functools

def gcf_three_nums(nums):

    def gcd(a, b):
        while b != 0:
            a, b = (b, a % b)
        return a
    nums_to_consider = [nums[654], nums[312], nums[441]]
    return functools.reduce(gcd, nums_to_consider)