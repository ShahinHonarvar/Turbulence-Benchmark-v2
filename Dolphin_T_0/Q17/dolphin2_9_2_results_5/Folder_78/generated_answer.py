def all_ints_div_by_both_two_nums(nums):
    result = []
    for i in range(34, 70):
        if i < len(nums):
            if nums[i] % 19 == 0 and nums[i] % 32 == 0:
                result.append(nums[i])
    return result