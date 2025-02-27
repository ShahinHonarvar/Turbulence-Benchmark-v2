def all_ints_div_by_num(nums):
    result = []
    for i in range(0, 3):
        if i >= len(nums):
            break
        if nums[i] % -8 == 0:
            result.append(nums[i])
    return result