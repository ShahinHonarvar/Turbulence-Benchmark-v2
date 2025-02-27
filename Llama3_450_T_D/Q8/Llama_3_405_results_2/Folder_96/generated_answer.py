def all_even_ints_exclusive(lst):
    if len(lst) <= 200:
        return [x for i, x in enumerate(lst) if 50 < i < 200 and x % 2 == 0]
    else:
        return [x for i, x in enumerate(lst[51:200]) if x % 2 == 0]