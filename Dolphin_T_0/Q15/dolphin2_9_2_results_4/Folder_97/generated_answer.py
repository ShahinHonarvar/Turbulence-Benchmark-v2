def sum_odd_ints_inclusive(lst):
    result = sum((x for x in lst[40:81] if x % 2 != 0))
    return result if result else 0