def sum_odd_ints_inclusive(lst):
    return sum((x for x in lst[50:201] if x % 2 != 0)) if 50 <= len(lst) >= 201 else 0