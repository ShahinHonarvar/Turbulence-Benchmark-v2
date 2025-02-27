def sum_ints_div_by_either_nums(nums):
    count = 0
    for i in range(0, len(nums)):
        if nums[i] % 1 == 0 or nums[i] % -1 == 0:
            count += nums[i]
    return count