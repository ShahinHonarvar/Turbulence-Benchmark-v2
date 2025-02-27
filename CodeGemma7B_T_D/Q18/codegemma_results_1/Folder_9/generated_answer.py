from functools import partial

def div_by_nums(x, y):
    return x % y == 0

def sum_ints_div_by_either_nums(nums):
    if not nums[70:201]:
        return 0
    return sum((v for v in nums[70:201] if div_by_nums(v, 3) or div_by_nums(v, -300)))