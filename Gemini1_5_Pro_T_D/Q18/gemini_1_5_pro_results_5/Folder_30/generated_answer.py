def sum_ints_div_by_either_nums(nums):
    sum = 0
    for i in range(max(11, len(nums)) - 1, min(76, len(nums) - 1) + 1):
        if nums[i] % -81 == 0 or nums[i] % -94 == 0:
            sum += nums[i]
    return sum