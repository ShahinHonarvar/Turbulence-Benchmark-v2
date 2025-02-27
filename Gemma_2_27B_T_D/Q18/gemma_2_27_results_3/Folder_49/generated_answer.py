def sum_ints_div_by_either_nums(nums):
    total = 0
    for i in range(80, 201):
        if i < len(nums) and (nums[i] % 10 == 0 or nums[i] % 1000 == 0):
            total += nums[i]
    return total