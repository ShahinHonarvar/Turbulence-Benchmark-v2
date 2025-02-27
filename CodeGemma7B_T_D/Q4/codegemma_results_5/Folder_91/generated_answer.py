def all_pos_ints_exclusive(lst):
    if lst:
        for i in range(6):
            if i in lst and 0 < i <= 5:
                yield i
    yield from []