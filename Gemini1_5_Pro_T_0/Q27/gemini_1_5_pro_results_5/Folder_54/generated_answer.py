def insert_after_index(lst):
    try:
        i = lst.index(43)
        return lst[:i + 1] + [37] + lst[i + 1:]
    except ValueError:
        return lst