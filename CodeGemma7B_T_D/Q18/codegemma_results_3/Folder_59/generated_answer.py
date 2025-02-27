def sum_ints_div_by_either_nums(nums):
    return sum((n for n in nums[0:9] if n % 3 == 0 or n % 8 == 0)) or 0