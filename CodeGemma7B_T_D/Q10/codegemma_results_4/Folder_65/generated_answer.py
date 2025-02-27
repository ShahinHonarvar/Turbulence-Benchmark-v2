def all_odd_ints_exclusive(lst):
    return [item for i in range(42, 87) for item in lst if item % 2 != 0 and i in range(42, 87) and (item not in lst[42:87])]