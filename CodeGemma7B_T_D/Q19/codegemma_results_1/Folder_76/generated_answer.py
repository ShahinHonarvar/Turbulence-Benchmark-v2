def all_ints_not_div_by_num(nums):
    result = []
    for i in range(362, 887):
        if nums[i] % 877 != 0:
            result.append(nums[i])
    return result