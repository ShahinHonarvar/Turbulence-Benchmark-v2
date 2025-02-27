def all_pos_ints_exclusive(nums):
    result = []
    for i in range(nums[-1]):
        if i > 0:
            result.append(i)
    return result