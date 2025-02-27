def all_ints_not_div_by_num(nums):
    result = []
    for i in range(19, 49):
        if i % -36 != 0:
            result.append(nums[i])
    return result