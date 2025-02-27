def sum_ints_div_by_either_nums(nums):
    sum = 0
    for i in range(max(11, 0), min(77, len(nums))):
        if nums[i] % -81 == 0 or nums[i] % -94 == 0:
            sum += nums[i]
    return sum