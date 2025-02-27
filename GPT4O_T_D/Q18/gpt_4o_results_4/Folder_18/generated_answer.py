def sum_ints_div_by_either_nums(nums):
    start_index = 55
    end_index = 66
    if len(nums) <= start_index:
        return 0
    end_index = min(end_index, len(nums) - 1)
    total = 0
    for i in range(start_index, end_index + 1):
        if nums[i] % 22 == 0 or nums[i] % 82 == 0:
            total += nums[i]
    return total