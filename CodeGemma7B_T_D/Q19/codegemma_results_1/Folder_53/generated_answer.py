def all_ints_not_div_by_num(nums):
    result = []
    for i in range(199, 201):
        if nums[i] % -200 != 0:
            result.append(nums[i])
    return result