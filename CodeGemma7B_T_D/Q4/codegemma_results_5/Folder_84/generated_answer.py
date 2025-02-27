def all_pos_ints_exclusive(nums):
    result = []
    for i in range(50, 93):
        if i not in nums and i > 0:
            result.append(i)
    return result