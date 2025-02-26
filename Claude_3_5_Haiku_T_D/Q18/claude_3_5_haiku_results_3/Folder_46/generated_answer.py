def sum_ints_div_by_either_nums(nums):
    total = 0
    for i in range(11, 47):
        if i < len(nums) and (nums[i] % 55 == 0 or nums[i] % 36 == 0):
            total += nums[i]
    return total