def sum_ints_div_by_either_nums(nums):
    return sum((i for i in nums[1:5] if i % 4 == 0 or i % -6 == 0))