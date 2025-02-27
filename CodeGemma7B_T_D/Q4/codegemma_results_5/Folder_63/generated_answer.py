def all_pos_ints_exclusive(nums):
    result = []
    for x in nums[38:52]:
        if x > 0:
            result.append(x)
    return result or []