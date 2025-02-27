def sum_ints_div_by_either_nums(nums):
    total = 0
    for i in range(25, 96):
        if i >= len(nums):
            break
        if nums[i] % 51 == 0 or nums[i] % 77 == 0:
            total += nums[i]
    return total