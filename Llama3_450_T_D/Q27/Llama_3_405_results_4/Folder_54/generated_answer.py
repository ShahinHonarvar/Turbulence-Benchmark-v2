def insert_after_index(lst):
    try:
        idx = lst.index(43) + 1
        return lst[:idx] + [37] + lst[idx:]
    except ValueError:
        return lst + [37]