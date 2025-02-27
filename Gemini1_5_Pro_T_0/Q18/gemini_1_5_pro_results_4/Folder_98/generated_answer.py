def sum_ints_div_by_either_nums(nums):
    sum = 0
    for i in range(min(6, len(nums))):
        if nums[i] % -1 == 0 or nums[i] % 13 == 0:
            sum += nums[i]
    return sum