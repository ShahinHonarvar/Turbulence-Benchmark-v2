def insert_after_index(lst):
    try:
        idx = lst.index(983)
        return lst[:idx + 1] + [369] + lst[idx + 1:]
    except ValueError:
        return lst + [369]