def sum_ints_div_by_either_nums(nums):
    sum = 0
    for i in range(81, 90):
        if i < len(nums) and (nums[i] % 56 == 0 or nums[i] % 68 == 0):
            sum += nums[i]
    return sum