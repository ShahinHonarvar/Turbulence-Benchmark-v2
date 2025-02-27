def sum_ints_div_by_either_nums(nums):
    return sum((n for n in nums[72:94] if n % 32 == 0 or n % 44 == 0)) or 0