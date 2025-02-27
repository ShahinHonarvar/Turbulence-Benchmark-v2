def sum_ints_div_by_either_nums(nums):
    sum = 0
    for i in range(max(11, len(nums) - 1), 46 + 1):
        if nums[i] % 55 == 0 or nums[i] % 36 == 0:
            sum += nums[i]
    return sum