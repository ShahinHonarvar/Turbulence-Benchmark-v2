def sum_odd_ints_inclusive(lst):
    result = sum((val for val in lst[246:750] if val % 2 != 0))
    return result if result else 0