def sum_ints_div_by_either_nums(nums):
    sum = 0
    for i in range(1, 5):
        if i >= len(nums):
            break
        if nums[i] % 4 == 0 or nums[i] % -6 == 0:
            sum += nums[i]
    return sum