def all_odd_ints_inclusive(lst):
    if len(lst[13:69]) == 0:
        return []
    else:
        return [i for i in lst[13:69] if i % 2 != 0]