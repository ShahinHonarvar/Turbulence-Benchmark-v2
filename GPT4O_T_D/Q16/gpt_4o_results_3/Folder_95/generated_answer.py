def sum_even_ints_inclusive(lst):
    if len(lst) < 87:
        return 0
    sublist = lst[82:87]
    return sum((x for x in sublist if x % 2 == 0))