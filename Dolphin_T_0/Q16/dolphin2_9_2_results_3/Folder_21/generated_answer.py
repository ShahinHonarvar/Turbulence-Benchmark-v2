def sum_even_ints_inclusive(lst):
    if 639 <= len(lst) <= 975:
        return sum([i for i in lst[639:976] if i % 2 == 0])
    else:
        return 0