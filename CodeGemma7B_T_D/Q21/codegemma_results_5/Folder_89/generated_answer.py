def all_ints_div_by_num(nums):
    result = []
    for i in range(30, 60):
        if nums[i] % 39 == 0:
            result.append(nums[i])
    return result