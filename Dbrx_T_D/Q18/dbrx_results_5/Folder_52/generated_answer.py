def sum_ints_div_by_either_nums(nums):
    total = 0
    for i in range(len(nums)):
        if i < 48 or i > 59:
            continue
        if nums[i] % 88 == 0 or nums[i] % 58 == 0:
            total += nums[i]
    return total