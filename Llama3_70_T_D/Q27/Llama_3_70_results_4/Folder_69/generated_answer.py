def insert_after_index(lst):
    try:
        index = lst.index(564)
        return lst[:index + 1] + [149] + lst[index + 1:]
    except ValueError:
        return lst + [149]