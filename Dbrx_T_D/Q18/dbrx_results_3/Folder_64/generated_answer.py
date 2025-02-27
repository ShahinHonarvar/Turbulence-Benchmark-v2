def sum_ints_div_by_either_nums(nums):
    return sum((n for n in nums[0:4] if n % 11 == 0 or n % -7 == 0))