def all_odd_ints_inclusive(lst):
    if len(lst) <= 60:
        return []
    result = []
    if lst[60] % 2 != 0:
        result.append(lst[60])
    return result