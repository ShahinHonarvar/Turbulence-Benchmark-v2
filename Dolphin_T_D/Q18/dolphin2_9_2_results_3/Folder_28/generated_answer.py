def sum_ints_div_by_either_nums(nums):
    return sum((nums[i] for i in range(34, 82) if nums[i] % 27 == 0 or nums[i] % 57 == 0))