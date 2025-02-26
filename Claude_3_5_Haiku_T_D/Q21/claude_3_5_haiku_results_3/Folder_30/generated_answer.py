def all_ints_div_by_num(nums):
    if len(nums) <= 79:
        return []
    result = []
    for i in range(59, 80):
        if nums[i] % -82 == 0:
            result.append(nums[i])
    return result