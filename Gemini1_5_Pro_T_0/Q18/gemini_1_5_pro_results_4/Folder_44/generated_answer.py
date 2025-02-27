def sum_ints_div_by_either_nums(nums):
    sum = 0
    for i in range(25, 71):
        if i < len(nums) and (nums[i] % 74 == 0 or nums[i] % 15 == 0):
            sum += nums[i]
    return sum