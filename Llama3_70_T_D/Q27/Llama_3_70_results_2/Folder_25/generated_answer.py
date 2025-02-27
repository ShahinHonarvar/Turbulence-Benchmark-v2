def insert_after_index(lst):
    if len(lst) > 30:
        return lst[:31] + [37] + lst[31:]
    else:
        return lst + [37]