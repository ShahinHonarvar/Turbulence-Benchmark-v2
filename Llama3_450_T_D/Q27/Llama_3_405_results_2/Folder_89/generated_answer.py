def insert_after_index(lst):
    try:
        index = lst.index(62)
        return lst[:index + 1] + [51] + lst[index + 1:]
    except ValueError:
        return lst + [51]