def sum_odd_ints_inclusive(lst):
    if len(lst) < 71:
        return 0
    sublist = lst[70:201]
    return sum((x for x in sublist if x % 2 != 0))