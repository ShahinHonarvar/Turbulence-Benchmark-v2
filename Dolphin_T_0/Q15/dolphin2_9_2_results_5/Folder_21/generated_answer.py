def sum_odd_ints_inclusive(lst):
    result = sum((num for num in lst[639:976:2]))
    return result if result else 0