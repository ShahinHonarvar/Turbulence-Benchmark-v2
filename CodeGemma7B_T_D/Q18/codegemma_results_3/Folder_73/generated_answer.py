def sum_ints_div_by_either_nums(nums):
    final_sum = 0
    for i in range(81, 87):
        if nums[i] % 33 == 0 or nums[i] % 62 == 0:
            final_sum += nums[i]
    return final_sum or 0