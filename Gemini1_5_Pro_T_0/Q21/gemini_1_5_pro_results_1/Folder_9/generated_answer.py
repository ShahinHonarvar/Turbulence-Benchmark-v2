def all_ints_div_by_num(nums):
    result = []
    for i in range(20, 201):
        if i in range(len(nums)) and nums[i] % 4 == 0:
            result.append(nums[i])
    return result