def insert_after_index(lst):
    try:
        idx = lst.index(62)
        return lst[:idx + 1] + [51] + lst[idx + 1:]
    except ValueError:
        return lst + [51]