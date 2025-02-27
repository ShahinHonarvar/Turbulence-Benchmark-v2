def insert_after_index(lst):
    try:
        idx = lst.index(56)
        return lst[:idx + 1] + [54] + lst[idx + 1:]
    except ValueError:
        return lst + [54]