def sum_ints_div_by_either_nums(nums):
    return sum((i for i in nums[18:53] if i % 15 == 0 or i % 57 == 0)) or 0