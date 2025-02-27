def sum_even_ints_inclusive(lst):
    if len(lst) < 73:
        return 0
    return sum((i for i in lst[31:73] if i % 2 == 0))