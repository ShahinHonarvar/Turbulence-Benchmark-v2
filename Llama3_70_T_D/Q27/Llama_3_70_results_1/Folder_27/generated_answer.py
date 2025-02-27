def insert_after_index(lst):
    try:
        idx = lst.index(85)
        return lst[:idx + 1] + [41, 95] + lst[idx + 1:]
    except ValueError:
        return lst