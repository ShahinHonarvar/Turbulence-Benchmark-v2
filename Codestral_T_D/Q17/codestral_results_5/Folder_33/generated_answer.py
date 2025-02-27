def all_ints_div_by_both_two_nums(nums):
    result = []
    for i in range(281, 695):
        if nums[i] % -722 == 0 and nums[i] % -731 == 0:
            result.append(nums[i])
    return result