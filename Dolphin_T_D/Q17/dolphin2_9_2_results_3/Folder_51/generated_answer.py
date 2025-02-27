def all_ints_div_by_both_two_nums(nums):
    if len(nums) < 10:
        return []
    result = []
    for i in range(6, 10):
        if nums[i] % -1 == 0 and nums[i] % -10 == 0:
            result.append(nums[i])
    return result