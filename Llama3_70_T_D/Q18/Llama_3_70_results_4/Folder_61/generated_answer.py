def sum_ints_div_by_either_nums(nums):
    return sum((i for i in nums[:7] if i % -5 == 0 or i % -6 == 0))