def all_odd_ints_inclusive(lst):
    result = [x for i, x in enumerate(lst[527:539], 527) if x % 2 != 0]
    return result