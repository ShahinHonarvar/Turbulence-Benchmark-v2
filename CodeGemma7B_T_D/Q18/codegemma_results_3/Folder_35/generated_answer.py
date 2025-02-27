def sum_ints_div_by_either_nums(nums):
    return sum((n for n in nums[77:88] if n % 23 == 0 or n % 57 == 0)) or 0