def sum_ints_div_by_either_nums(nums):
    total = 0
    for i in range(61, 89):
        if i >= len(nums):
            break
        if nums[i] % 31 == 0 or nums[i] % 11 == 0:
            total += nums[i]
    return total