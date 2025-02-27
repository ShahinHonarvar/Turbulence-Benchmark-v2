def all_pos_ints_exclusive(nums):
    result = []
    for i in range(7):
        if i > 0 and i not in nums:
            result.append(i)
    return result