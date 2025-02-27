def all_odd_ints_inclusive(lst):
    odd_ints = [x for x in lst[56:67] if x % 2 != 0]
    if len(odd_ints) > 0:
        return odd_ints
    else:
        return []