def sum_even_ints_inclusive(lst):
    if len(lst) < 69:
        return 0
    else:
        return sum((i for i in lst[13:69] if i % 2 == 0))