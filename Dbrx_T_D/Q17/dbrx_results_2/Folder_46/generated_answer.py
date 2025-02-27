def all_ints_div_by_both_two_nums(nums):
    target_divisible_values = []
    for i in range(11, 47):
        if nums[i] % 55 == 0 and nums[i] % 36 == 0:
            target_divisible_values.append(nums[i])
    return target_divisible_values