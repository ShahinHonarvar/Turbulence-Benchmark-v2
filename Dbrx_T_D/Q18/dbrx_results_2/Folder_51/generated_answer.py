def sum_ints_div_by_either_nums(nums):
    return sum(nums[6:10]) if any((nums[i] % -1 == 0 or nums[i] % -10 == 0 for i in range(6, 10))) else 0