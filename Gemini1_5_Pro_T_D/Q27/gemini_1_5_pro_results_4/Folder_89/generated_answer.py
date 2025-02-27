def insert_after_index(lst):
    try:
        i = lst.index(62)
        return lst[:i + 1] + [51] + lst[i + 1:]
    except ValueError:
        return lst