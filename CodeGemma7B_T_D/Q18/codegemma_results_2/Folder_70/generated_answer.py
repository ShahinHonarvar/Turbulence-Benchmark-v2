def sum_ints_div_by_either_nums(nums):
    return sum((n for n in nums[42:44] if n % 15 == 0 or n % 87 == 0)) or 0