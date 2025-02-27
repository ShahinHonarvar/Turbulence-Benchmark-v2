def all_pos_ints_inclusive(nums):
    result = []
    for num in range(len(nums)):
        if num in range(9):
            if num >= 0:
                result.append(num)
    return result