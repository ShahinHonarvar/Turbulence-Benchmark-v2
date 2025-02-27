def sum_ints_div_by_either_nums(nums):
    return sum((nums[i] for i in range(81, 87) if nums[i] % -33 == 0 or nums[i] % -62 == 0))