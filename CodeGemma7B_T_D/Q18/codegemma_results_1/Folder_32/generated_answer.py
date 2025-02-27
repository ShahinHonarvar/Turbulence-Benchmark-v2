def sum_ints_div_by_either_nums(nums):
    return sum((n for n in nums[25:96] if n % 51 == 0 or n % 77 == 0)) or 0