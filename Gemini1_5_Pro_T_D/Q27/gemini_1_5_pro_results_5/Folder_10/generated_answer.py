def insert_after_index(lst):
    try:
        i = lst.index(56)
        return lst[:i + 1] + [54] + lst[i + 1:]
    except ValueError:
        return lst