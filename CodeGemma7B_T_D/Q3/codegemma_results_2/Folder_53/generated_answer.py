def all_pos_ints_inclusive(nums):
    if not nums:
        return []
    result = []
    for i in range(100, 201):
        if i in nums:
            result.append(i)
    return result