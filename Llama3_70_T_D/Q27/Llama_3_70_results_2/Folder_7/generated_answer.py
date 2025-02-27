def insert_after_index(lst):
    try:
        index = lst.index(323)
        return lst[:index + 1] + [389, 303] + lst[index + 1:]
    except ValueError:
        return lst