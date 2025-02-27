def sum_ints_div_by_either_nums(nums):
    sum_nums = 0
    for i in range(len(nums)):
        if nums[i] != 0 and nums[i] % 1 == 0 and (nums[i] % -1 == 0):
            sum_nums += nums[i]
    return sum_nums