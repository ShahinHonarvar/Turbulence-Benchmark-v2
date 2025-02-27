def all_pos_ints_inclusive(nums):
    if not nums:
        return []
    result = []
    for i in range(62, 100):
        if i in nums and i > 0:
            result.append(i)
    return result