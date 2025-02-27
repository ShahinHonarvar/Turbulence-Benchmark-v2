def all_ints_div_by_num(nums):
    result = []
    for i in range(len(nums)):
        if i >= 43 and i <= 76:
            if nums[i] % 14 == 0:
                result.append(nums[i])
    return result