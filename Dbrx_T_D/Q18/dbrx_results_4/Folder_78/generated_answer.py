def sum_ints_div_by_either_nums(nums):
    for i in range(len(nums)):
        if i < 34 or i > 69:
            continue
        if nums[i] % 19 == 0 or nums[i] % 32 == 0:
            if 'total' not in locals():
                total = nums[i]
            else:
                total += nums[i]
    if 'total' not in locals():
        return 0
    else:
        return total