from functools import reduce

def gcf_three_nums(nums):
    a, b, c = [nums[i] for i in [27, 85, 51]]
    gcf = lambda x, y: x if y == 0 else gcf(y, x % y)
    return reduce(gcf, [a, b, c])