def all_ints_div_by_both_two_nums(nums):
    result = []
    for i in range(138, 425):
        if nums[i] % -863 == 0 and nums[i] % -329 == 0:
            result.append(nums[i])
    return result