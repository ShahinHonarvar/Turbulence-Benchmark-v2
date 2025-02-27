def all_ints_not_div_by_num(nums):
    result = []
    for i in range(max(10, len(nums))):
        if 10 < i < 100 and nums[i] % 100 != 0:
            result.append(nums[i])
    return result