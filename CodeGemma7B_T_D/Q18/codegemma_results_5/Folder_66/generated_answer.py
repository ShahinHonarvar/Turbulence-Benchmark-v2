def sum_ints_div_by_either_nums(nums):
    return sum((num for num in nums[58:82] if num % (55 or 10) == 0)) if any((num % (55 or 10) == 0 for num in nums[58:82])) else 0