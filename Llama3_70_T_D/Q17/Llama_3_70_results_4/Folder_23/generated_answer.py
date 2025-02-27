def all_ints_div_by_both_two_nums(nums):
    result = []
    for i in range(69, 98):
        if nums[i] % -90 == 0 and nums[i] % -67 == 0:
            result.append(nums[i])
    return result