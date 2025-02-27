def sum_ints_div_by_either_nums(nums):
    total = 0
    for i in range(34, 82):
        if i < len(nums) and (nums[i] % 27 == 0 or nums[i] % 57 == 0):
            total += nums[i]
    return total