def sum_ints_div_by_either_nums(nums):
    if len(nums) < 44:
        return 0
    sum_result = 0
    for i in range(42, 44):
        if nums[i] % 15 == 0 or nums[i] % 87 == 0:
            sum_result += nums[i]
    return sum_result