def insert_after_index(lst):
    try:
        idx = lst.index(89)
        return lst[:idx + 1] + [86] + lst[idx + 1:]
    except ValueError:
        return lst