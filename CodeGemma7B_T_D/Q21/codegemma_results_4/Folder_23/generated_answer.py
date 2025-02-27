def all_ints_div_by_num(nums):
    result = []
    for i in range(59, 98):
        if nums[i] % -36 == 0:
            result.append(nums[i])
    return result