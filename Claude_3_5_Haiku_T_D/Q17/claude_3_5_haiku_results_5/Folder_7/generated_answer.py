def all_ints_div_by_both_two_nums(nums):
    result = []
    for i in range(543, 585):
        if i < len(nums):
            if nums[i] % -553 == 0 and nums[i] % -737 == 0:
                result.append(nums[i])
    return result