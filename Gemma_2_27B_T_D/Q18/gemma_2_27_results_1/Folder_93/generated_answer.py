def sum_ints_div_by_either_nums(nums):
    total = 0
    for i in range(86, 90):
        if i < len(nums) and (nums[i] % -61 == 0 or nums[i] % -79 == 0):
            total += nums[i]
    return total