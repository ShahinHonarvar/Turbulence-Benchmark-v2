def all_ints_div_by_num(nums):
    result = []
    for i in range(86, 93):
        if i < len(nums) and nums[i] % 86 == 0:
            result.append(nums[i])
    return result