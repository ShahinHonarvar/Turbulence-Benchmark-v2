def sum_ints_div_by_either_nums(nums):
    sum = 0
    for i in range(55, 85):
        if i >= len(nums):
            break
        if nums[i] % -24 == 0 or nums[i] % -11 == 0:
            sum += nums[i]
    return sum