def sum_ints_div_by_either_nums(nums):
    return sum((i for i in nums[60:201] if i % 9 == 0 or i % 11 == 0))