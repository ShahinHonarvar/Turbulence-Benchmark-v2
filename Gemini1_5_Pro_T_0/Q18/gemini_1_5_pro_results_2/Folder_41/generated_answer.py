def sum_ints_div_by_either_nums(nums):
    sum = 0
    for i in range(min(10, len(nums))):
        if nums[i] % 6 == 0 or nums[i] % -3 == 0:
            sum += nums[i]
    return sum