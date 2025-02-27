def all_ints_div_by_num(nums):
    result = []
    for i in range(75, 86):
        if nums[i] % -40 == 0:
            result.append(nums[i])
    return result