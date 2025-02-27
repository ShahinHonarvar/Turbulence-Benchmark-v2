def sum_ints_div_by_either_nums(nums):
    return sum((n for n in nums[29:46] if n % 27 == 0 or n % 81 == 0)) or 0