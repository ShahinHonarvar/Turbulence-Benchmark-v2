def sum_ints_div_by_either_nums(nums):
    sum = 0
    for i in range(57, 86):
        if i < len(nums) and (nums[i] % -77 == 0 or nums[i] % -32 == 0):
            sum += nums[i]
    return sum