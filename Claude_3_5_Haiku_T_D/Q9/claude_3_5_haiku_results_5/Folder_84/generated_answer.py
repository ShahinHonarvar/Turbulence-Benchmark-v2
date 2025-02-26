def all_odd_ints_inclusive(lst):
    if len(lst) <= 86:
        return []
    return [num for num in lst[43:87] if num % 2 != 0]