def sum_odd_ints_inclusive(lst):
    if len(lst) < 81:
        return 0
    return sum((x for x in lst[80:201] if x % 2 != 0))