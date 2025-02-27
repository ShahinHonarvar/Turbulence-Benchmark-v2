def sum_ints_div_by_either_nums(nums):
    sum = 0
    for i in range(57, 85):
        if i >= len(nums):
            break
        if nums[i] % -30 == 0 or nums[i] % -88 == 0:
            sum += nums[i]
    return sum