def insert_after_index(lst):
    try:
        idx = lst.index(696)
        return lst[:idx + 1] + [477] + lst[idx + 1:]
    except ValueError:
        return lst