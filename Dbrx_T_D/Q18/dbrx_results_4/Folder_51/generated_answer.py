def sum_ints_div_by_either_nums(nums):
    return sum((n for n in nums[6:10] if n % -1 == 0 or n % -10 == 0))