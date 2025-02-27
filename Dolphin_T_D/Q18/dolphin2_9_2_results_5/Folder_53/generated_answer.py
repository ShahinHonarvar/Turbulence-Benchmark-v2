def sum_ints_div_by_either_nums(nums):
    return sum(nums[200:201] + [-i for i in nums[200:201] if i % 17 == 0 or i % -5 == 0])