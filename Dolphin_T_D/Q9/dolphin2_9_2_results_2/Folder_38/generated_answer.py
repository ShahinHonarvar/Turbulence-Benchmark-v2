def all_odd_ints_inclusive(lst):
    result = [i for i in lst[22:64:2]]
    if len(result) == 0:
        return []
    return result