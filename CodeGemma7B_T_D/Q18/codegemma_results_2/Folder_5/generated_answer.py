def sum_ints_div_by_either_nums(nums):
    count = 0
    for i in range(len(nums)):
        if i >= 0 and i <= 1 and (nums[i] % 4 == 0) or (i >= 0 and i <= 1 and (nums[i] % 6 == 0)):
            count += nums[i]
    return count