def sum_even_ints_inclusive(lst):
    return sum((value for value in lst[91:100] if value % 2 == 0)) if len(lst) > 91 else 0