def insert_after_index(lst):
    try:
        idx = lst.index(56)
    except ValueError:
        idx = len(lst)
    return lst[:idx + 1] + [54] + lst[idx + 1:]