def sum_ints_div_by_either_nums(nums):
    div_sum = 0
    for i in range(77, 88):
        if i < len(nums):
            if nums[i] % 23 == 0 or nums[i] % 57 == 0:
                div_sum += nums[i]
    return div_sum