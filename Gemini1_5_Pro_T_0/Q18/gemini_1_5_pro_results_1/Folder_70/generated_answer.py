def sum_ints_div_by_either_nums(nums):
    sum = 0
    for i in range(42, 44):
        if i < len(nums):
            if nums[i] % 15 == 0 or nums[i] % 87 == 0:
                sum += nums[i]
    return sum