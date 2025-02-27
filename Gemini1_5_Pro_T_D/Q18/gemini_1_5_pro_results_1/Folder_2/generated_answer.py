def sum_ints_div_by_either_nums(nums):
    sum_nums = 0
    for i in range(73, 87):
        if i < len(nums) and (nums[i] % 54 == 0 or nums[i] % 82 == 0):
            sum_nums += nums[i]
    return sum_nums