def sum_ints_div_by_either_nums(nums):
    sum = 0
    for i in range(34, 82):
        if i < len(nums) and (nums[i] % 27 == 0 or nums[i] % 57 == 0):
            sum += nums[i]
    return sum