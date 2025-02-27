def sum_ints_div_by_either_nums(nums):
    total = 0
    if 0 <= 0 and 0 >= 0 and (nums[0] % 1 == 0 or nums[0] % -1 == 0):
        total += nums[0]
    return total