def sum_ints_div_by_either_nums(nums):
    total = 0
    for i in range(34, 70):
        if i < len(nums) and (nums[i] % 19 == 0 or nums[i] % 32 == 0):
            total += nums[i]
    return total