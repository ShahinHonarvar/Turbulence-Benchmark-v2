def all_ints_div_by_num(nums):
    result = []
    for i in range(min(3, len(nums))):
        if nums[i] % 3 == 0:
            result.append(nums[i])
    return result