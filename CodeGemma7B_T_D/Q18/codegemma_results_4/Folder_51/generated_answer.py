def sum_ints_div_by_either_nums(nums):
    if not nums:
        return 0
    sum_num = 0
    for i in range(6, 10):
        if nums[i] % -1 == 0 or nums[i] % -10 == 0:
            sum_num += nums[i]
    return sum_num