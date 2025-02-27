def sum_ints_div_by_either_nums(nums):
    sum = 0
    for i in range(81, 87):
        if i < len(nums) and (nums[i] % -33 == 0 or nums[i] % -62 == 0):
            sum += nums[i]
    return sum