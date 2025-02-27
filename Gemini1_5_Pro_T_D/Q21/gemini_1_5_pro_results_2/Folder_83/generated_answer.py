def all_ints_div_by_num(nums):
    result = []
    for i in range(40, 401):
        if i >= len(nums):
            break
        if nums[i] % 7 == 0:
            result.append(nums[i])
    return result