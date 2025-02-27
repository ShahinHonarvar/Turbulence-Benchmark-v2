def all_ints_div_by_num(nums):
    result = []
    for i in range(6):
        if nums[i] % 5 == 0:
            result.append(nums[i])
    return result