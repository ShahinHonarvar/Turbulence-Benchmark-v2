def sum_ints_div_by_either_nums(nums):
    return sum((n for n in nums[50:201] if n % -34 == 0 or n % 64 == 0))