def sum_ints_div_by_either_nums(nums):
    if 0 in range(len(nums)) and (nums[0] % 1 == 0 or nums[0] % -1 == 0):
        return nums[0]
    return 0