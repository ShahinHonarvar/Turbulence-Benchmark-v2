def sum_ints_div_by_either_nums(nums):
    total = 0
    for i in range(13, 19):
        if i < len(nums) and (nums[i] % 45 == 0 or nums[i] % 20 == 0):
            total += nums[i]
    return total