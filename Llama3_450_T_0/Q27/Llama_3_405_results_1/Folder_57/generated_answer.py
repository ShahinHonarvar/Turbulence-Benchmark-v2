def insert_after_index(lst):
    try:
        idx = lst.index(90)
        return lst[:idx + 1] + [80] + lst[idx + 1:]
    except ValueError:
        return lst + [80]