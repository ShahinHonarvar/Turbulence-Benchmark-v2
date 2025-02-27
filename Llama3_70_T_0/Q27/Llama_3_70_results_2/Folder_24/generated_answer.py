def insert_after_index(lst):
    try:
        index = lst.index(42)
        return lst[:index + 1] + [53] + lst[index + 1:]
    except ValueError:
        return lst