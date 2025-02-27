def sum_ints_div_by_either_nums(nums):
    if nums and isinstance(nums[0], int) and isinstance(nums[1], int):
        return nums[0] + nums[1]
    else:
        return 0