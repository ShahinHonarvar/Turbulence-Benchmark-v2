def sum_ints_div_by_either_nums(nums):
    total = 0
    for i in range(7, 10):
        if i < len(nums) and (nums[i] % -9 == 0 or nums[i] % -7 == 0):
            total += nums[i]
    return total