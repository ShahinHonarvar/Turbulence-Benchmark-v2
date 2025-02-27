def sum_ints_div_by_either_nums(nums):
    count = sum((n % 11 in (0, -7) or n % 7 in (0, -7) for n in nums[0:4]))
    return count if count else 0