def insert_after_index(lst):
    try:
        index = lst.index(99)
        return lst[:index + 1] + [99] + lst[index + 1:]
    except ValueError:
        return lst