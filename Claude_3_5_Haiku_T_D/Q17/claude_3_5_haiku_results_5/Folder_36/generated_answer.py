def all_ints_div_by_both_two_nums(nums):
    result = []
    for i in range(299, 383):
        if i < len(nums) and nums[i] % 858 == 0 and (nums[i] % 952 == 0):
            result.append(nums[i])
    return result