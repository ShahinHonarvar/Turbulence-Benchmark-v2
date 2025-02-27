def insert_after_index(lst):
    try:
        index = lst.index(43)
        return lst[:index + 1] + [37] + lst[index + 1:]
    except ValueError:
        return lst + [37]