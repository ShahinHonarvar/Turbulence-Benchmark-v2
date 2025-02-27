def all_ints_div_by_num(nums):
    result = []
    for i in range(max(0, min(40, len(nums))), min(401, len(nums))):
        if nums[i] % 7 == 0:
            result.append(nums[i])
    return result