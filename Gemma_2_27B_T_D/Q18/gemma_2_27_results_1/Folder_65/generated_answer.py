def sum_ints_div_by_either_nums(nums):
    return sum((n for n in nums[50:93] if n % -94 == 0 or n % -95 == 0))