def all_even_ints_inclusive(lst):
    if len(lst) < 72:
        return []
    else:
        return [i for i in lst[31:73] if i % 2 == 0]