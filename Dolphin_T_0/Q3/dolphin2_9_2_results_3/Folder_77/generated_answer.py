def all_pos_ints_inclusive(lst):
    result = [num for i, num in enumerate(lst[527:539], start=527) if num > 0]
    return result if result else []