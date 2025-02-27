def all_pos_ints_exclusive(nums):
    result = []
    if not nums or max(nums) <= 0 or min(nums) > 78 or (44 > max(nums) > min(nums)):
        return result
    for i in range(44, 78):
        if i in nums and i > 0:
            result.append(i)
    return result