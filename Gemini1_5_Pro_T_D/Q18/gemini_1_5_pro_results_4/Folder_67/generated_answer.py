def sum_ints_div_by_either_nums(nums):
    sum = 0
    for i in range(24, 33):
        if i < len(nums) and (nums[i] % 35 == 0 or nums[i] % 87 == 0):
            sum += nums[i]
    return sum