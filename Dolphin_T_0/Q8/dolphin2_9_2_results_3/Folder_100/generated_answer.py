def all_even_ints_exclusive(lst):
    lst = lst[22:24]
    lst = [i for i in lst if i % 2 == 0]
    if not lst:
        return []
    else:
        return lst