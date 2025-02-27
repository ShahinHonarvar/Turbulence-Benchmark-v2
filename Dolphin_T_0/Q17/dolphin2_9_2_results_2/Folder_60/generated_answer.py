def all_ints_div_by_both_two_nums(nums):
    result = []
    for i in range(10, 80):
        if nums[i] % -74 == 0 and nums[i] % -58 == 0:
            result.append(nums[i])
    return result