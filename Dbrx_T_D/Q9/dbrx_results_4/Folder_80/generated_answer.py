def all_odd_ints_inclusive(lst):
    if len(lst) < 66:
        return []
    elif len(lst) == 66:
        return [i for i in lst[63:67] if i % 2 != 0]
    else:
        return [i for i in lst[64:67] if i % 2 != 0]