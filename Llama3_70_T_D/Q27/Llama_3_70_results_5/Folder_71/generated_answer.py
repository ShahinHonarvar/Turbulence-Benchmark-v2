def insert_after_index(lst):
    try:
        idx = lst.index(70)
        return lst[:idx + 1] + [76] + lst[idx + 1:]
    except ValueError:
        return lst