def all_odd_ints_inclusive(lst):
    result = [i for i in lst[661:925] if i % 2 != 0]
    if len(result) == 0:
        return []
    else:
        return result