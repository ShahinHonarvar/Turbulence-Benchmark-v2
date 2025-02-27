def insert_after_index(lst):
    try:
        idx = lst.index(74)
        return lst[:idx + 1] + [49] + lst[idx + 1:]
    except ValueError:
        return lst