def all_ints_div_by_num(nums):
    if not nums:
        return []
    result = []
    for i in range(10, 53):
        if nums[i] % -12 == 0:
            result.append(nums[i])
    return result