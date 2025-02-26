def insert_after_index(lst):
    try:
        index = lst.index(990)
        return lst[:index + 1] + [905, 742] + lst[index + 1:]
    except ValueError:
        return lst + [905, 742]