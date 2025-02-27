def insert_after_index(lst):
    if 43 in lst:
        return lst[:43 + 1] + [37] + lst[43 + 1:]
    else:
        return lst + [37]