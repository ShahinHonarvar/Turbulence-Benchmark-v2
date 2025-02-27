def sum_ints_div_by_either_nums(nums):
    sum = 0
    for i in range(306, 958):
        if i < len(nums) and (nums[i] % 982 == 0 or nums[i] % 319 == 0):
            sum += nums[i]
    return sum