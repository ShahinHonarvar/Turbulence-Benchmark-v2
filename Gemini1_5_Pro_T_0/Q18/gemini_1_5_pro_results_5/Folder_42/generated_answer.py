def sum_ints_div_by_either_nums(nums):
    sum = 0
    for i in range(29, 46):
        if i >= len(nums):
            break
        if nums[i] % 27 == 0 or nums[i] % 81 == 0:
            sum += nums[i]
    return sum