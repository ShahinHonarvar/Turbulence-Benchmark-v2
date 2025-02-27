from itertools import islice

def sum_ints_div_by_either_nums(nums):
    nums = nums[90:201]
    return sum(filter(lambda x: x % 31 == 0 or x % 13 == 0, nums))