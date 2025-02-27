def sum_ints_div_by_either_nums(nums):
    sum = 0
    for i in range(7, 10):
        if i < len(nums) and (nums[i] % 2 == 0 or nums[i] % 3 == 0):
            sum += nums[i]
    return sum