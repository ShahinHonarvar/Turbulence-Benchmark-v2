def sum_ints_div_by_either_nums(nums):
    if not nums or len(nums) < 121:
        return 0
    sum_nums = 0
    for i in range(25, 96):
        if nums[i] % 51 == 0 or nums[i] % 77 == 0:
            sum_nums += nums[i]
    return sum_nums