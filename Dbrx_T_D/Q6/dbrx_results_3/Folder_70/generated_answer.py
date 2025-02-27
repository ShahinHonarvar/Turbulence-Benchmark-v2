def all_neg_ints_exclusive(lst):
    try:
        return list(filter(lambda x: x < 0, lst[38:81]))
    except IndexError:
        return []