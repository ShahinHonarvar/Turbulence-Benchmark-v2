def all_ints_div_by_both_two_nums(nums):
    result = []
    for i in range(90, 98):
        if i < len(nums) and nums[i] % 13 == 0 and (nums[i] % 35 == 0):
            result.append(nums[i])
    return result