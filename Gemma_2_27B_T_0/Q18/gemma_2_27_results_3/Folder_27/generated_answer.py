def sum_ints_div_by_either_nums(nums):
    total = 0
    for i in range(20, 36):
        if i < len(nums) and (nums[i] % -36 == 0 or nums[i] % -89 == 0):
            total += nums[i]
    return total