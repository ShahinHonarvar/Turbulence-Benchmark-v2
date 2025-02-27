def sum_ints_div_by_either_nums(nums):
    return sum((n for i, n in enumerate(nums[81:87]) if i % 2 == 0 and n % -33 == 0 or (i % 2 == 1 and n % -62 == 0)))