def sum_ints_div_by_either_nums(nums):
    sum = 0
    for i in range(78, 82):
        if i < len(nums) and (nums[i] % 76 == 0 or nums[i] % 60 == 0):
            sum += nums[i]
    return sum