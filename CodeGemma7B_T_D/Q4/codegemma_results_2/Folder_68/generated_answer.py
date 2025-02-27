def all_pos_ints_exclusive(nums):
    result = []
    for i in range(9):
        if i not in nums:
            result.append(i)
    return result