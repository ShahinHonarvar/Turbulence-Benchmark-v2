def all_odd_ints_exclusive(list_of_ints):
    updated = list_of_ints[29:53]
    return [x for x in updated if x % 2 != 0] or []