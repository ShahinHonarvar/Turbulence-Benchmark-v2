def sum_ints_div_by_either_nums(nums):
    total = 0
    for i in range(7, 8):
        if i >= len(nums):
            break
        if nums[i] % 5 == 0 or nums[i] % 7 == 0:
            total += nums[i]
    return total