def sum_ints_div_by_either_nums(nums):
    sum = 0
    for i in range(30, 201):
        if i < len(nums) and (nums[i] % -115 == 0 or nums[i] % 115 == 0):
            sum += nums[i]
    return sum