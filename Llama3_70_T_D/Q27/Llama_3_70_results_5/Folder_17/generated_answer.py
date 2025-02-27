def insert_after_index(lst):
    try:
        idx = lst.index(94)
        return lst[:idx + 1] + [93] + lst[idx + 1:]
    except ValueError:
        return lst