def sum_ints_div_by_either_nums(nums):
    sum = 0
    for i in range(35, 65):
        if i < len(nums) and (nums[i] % -30 == 0 or nums[i] % -95 == 0):
            sum += nums[i]
    return sum