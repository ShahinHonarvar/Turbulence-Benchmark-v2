def sum_odd_ints_inclusive(lst):
    if len(lst) < 91:
        return 0
    return sum((x for x in lst[90:201] if x % 2 != 0))