def sum_ints_div_by_either_nums(nums):
    sum = 0
    for i in range(86, 90):
        if i < len(nums) and (nums[i] % -61 == 0 or nums[i] % -79 == 0):
            sum += nums[i]
    return sum