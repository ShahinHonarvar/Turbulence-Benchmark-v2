def sum_ints_div_by_either_nums(nums):
    sum = 0
    for i in range(11, 47):
        if i >= len(nums):
            break
        if nums[i] % 55 == 0 or nums[i] % 36 == 0:
            sum += nums[i]
    return sum