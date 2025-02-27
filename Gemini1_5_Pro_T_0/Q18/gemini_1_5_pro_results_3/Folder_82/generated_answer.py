def sum_ints_div_by_either_nums(nums):
    sum = 0
    for i in range(20, 201):
        if i >= len(nums):
            break
        if nums[i] % -20 == 0 or nums[i] % -200 == 0:
            sum += nums[i]
    return sum