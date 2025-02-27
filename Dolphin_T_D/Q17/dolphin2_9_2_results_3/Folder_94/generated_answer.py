def all_ints_div_by_both_two_nums(nums):
    result = []
    for i in range(93, 95):
        if nums[i] % -53 == 0 and nums[i] % -91 == 0:
            result.append(nums[i])
    return result