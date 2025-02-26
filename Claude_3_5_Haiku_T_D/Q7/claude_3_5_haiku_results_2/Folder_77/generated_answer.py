def all_even_ints_inclusive(lst):
    if len(lst) <= 538:
        return []
    return [x for x in lst[527:539] if x % 2 == 0]