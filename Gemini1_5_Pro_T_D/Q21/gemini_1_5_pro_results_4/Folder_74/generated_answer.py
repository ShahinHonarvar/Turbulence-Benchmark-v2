def all_ints_div_by_num(nums):
    result = []
    for i in range(62, 64):
        if i < len(nums) and nums[i] % 99 == 0:
            result.append(nums[i])
    return result