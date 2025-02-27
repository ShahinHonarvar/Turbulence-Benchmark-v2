def sum_ints_div_by_either_nums(nums):
    sum = 0
    for i in range(20, 94):
        if i >= len(nums):
            break
        if nums[i] % -92 == 0 or nums[i] % -50 == 0:
            sum += nums[i]
    return sum