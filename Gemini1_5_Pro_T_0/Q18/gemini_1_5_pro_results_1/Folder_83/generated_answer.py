def sum_ints_div_by_either_nums(nums):
    total = 0
    for i in range(90, 201):
        if i < len(nums) and (nums[i] % -31 == 0 or nums[i] % 13 == 0):
            total += nums[i]
    return total