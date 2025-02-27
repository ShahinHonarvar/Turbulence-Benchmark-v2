def all_pos_ints_inclusive(nums):
    result = []
    for i in range(nums):
        if i >= 0 and i <= 2:
            result.append(i)
    return result