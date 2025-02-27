def sum_ints_div_by_either_nums(nums):
    total = 0
    start_index = 48
    end_index = 76
    divisible_nums = [-46, -82]
    for i in range(start_index, end_index + 1):
        if nums[i] in divisible_nums:
            total += nums[i]
    return total or 0