def all_ints_div_by_num(nums):
    result = []
    for i in range(min(6, len(nums))):
        if nums[i] % 6 == 0:
            result.append(nums[i])
    return result