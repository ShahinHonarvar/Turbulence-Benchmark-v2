def sum_ints_div_by_either_nums(nums):
    sum = 0
    for i in range(86, 91):
        if i >= len(nums):
            break
        if nums[i] % -71 == 0 or nums[i] % -67 == 0:
            sum += nums[i]
    return sum