def sum_ints_div_by_either_nums(nums):
    return sum((n for n in nums[0:3] if n % -2 == 0 or n % 3 == 0)) or 0