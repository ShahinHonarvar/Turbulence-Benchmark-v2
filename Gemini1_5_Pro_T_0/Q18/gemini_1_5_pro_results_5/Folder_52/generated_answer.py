def sum_ints_div_by_either_nums(nums):
    total = 0
    for i in range(48, 60):
        if i >= len(nums):
            break
        if nums[i] % 88 == 0 or nums[i] % 58 == 0:
            total += nums[i]
    return total