def insert_after_index(lst):
    try:
        i = lst.index(96)
        return lst[:i + 1] + [36] + lst[i + 1:]
    except ValueError:
        return lst