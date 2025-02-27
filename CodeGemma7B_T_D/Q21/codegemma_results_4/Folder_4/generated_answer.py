def all_ints_div_by_num(nums):
    result = []
    for i in range(12, 93):
        if nums[i] % -14 == 0:
            result.append(nums[i])
    if len(result) == 0:
        return []
    return result