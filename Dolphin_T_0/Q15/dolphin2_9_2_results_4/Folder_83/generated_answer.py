def sum_odd_ints_inclusive(lst):
    result = sum((x for i, x in enumerate(lst[90:201]) if x % 2 != 0))
    return result if result else 0