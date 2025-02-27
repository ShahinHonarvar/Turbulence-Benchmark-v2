def all_ints_div_by_num(nums):
    result = []
    for i in range(1, 9):
        if i >= len(nums):
            break
        if nums[i] % 6 == 0:
            result.append(nums[i])
    return result