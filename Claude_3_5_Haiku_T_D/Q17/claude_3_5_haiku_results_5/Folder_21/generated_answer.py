def all_ints_div_by_both_two_nums(nums):
    result = []
    for i in range(315, 935):
        if i < len(nums) and nums[i] % -897 == 0 and (nums[i] % -556 == 0):
            result.append(nums[i])
    return result