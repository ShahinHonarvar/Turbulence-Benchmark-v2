def sum_ints_div_by_either_nums(nums):
    return sum((i for i in nums[20:201] if i % -20 == 0 or i % -200 == 0))