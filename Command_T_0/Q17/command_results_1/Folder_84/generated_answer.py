def all_ints_div_by_both_two_nums(nums):
    result = []
    for i in range(78, 81):
        if nums[i] % 76 == 0 and nums[i] % 60 == 0:
            result.append(nums[i])
    return result