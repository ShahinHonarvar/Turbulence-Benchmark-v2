def sum_even_ints_inclusive(lst):
    even_ints_sublist = lst[62:79:2]
    return sum(even_ints_sublist) if even_ints_sublist else 0