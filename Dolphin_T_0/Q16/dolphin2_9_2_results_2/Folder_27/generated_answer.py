def sum_even_ints_inclusive(lst):
    v = sum((x for i, x in enumerate(lst[66:94]) if i % 2 == 0))
    return v if v else 0