def all_ints_div_by_both_two_nums(nums):
    result = []
    for i in range(50, 201):
        if nums[i] % 34 == 0 and nums[i] % 64 == 0:
            result.append(nums[i])
    return result