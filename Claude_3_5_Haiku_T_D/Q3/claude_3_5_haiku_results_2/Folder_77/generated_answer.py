def all_pos_ints_inclusive(lst):
    if len(lst) <= 538:
        return []
    result = [num for num in lst[527:539] if num > 0]
    return result