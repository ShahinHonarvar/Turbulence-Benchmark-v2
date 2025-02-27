def all_pos_ints_exclusive(nums):
    result = []
    for i in range(9):
        if i not in nums and 1 <= i < 9:
            result.append(i)
    return result