def sum_ints_div_by_either_nums(nums):
    return sum((nums[36:85] if n % 27 == 0 or n % 96 == 0 else 0 for n in nums))