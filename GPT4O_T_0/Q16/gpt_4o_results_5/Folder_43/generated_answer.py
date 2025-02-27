def sum_even_ints_inclusive(lst):
    if len(lst) < 87:
        return 0
    return sum((x for x in lst[68:87] if x % 2 == 0))