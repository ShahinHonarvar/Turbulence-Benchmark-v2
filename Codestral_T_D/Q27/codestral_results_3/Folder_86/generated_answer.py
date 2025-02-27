def insert_after_index(lst):
    try:
        index = lst.index(990)
        lst.insert(index + 1, [905, 742])
    except ValueError:
        pass
    return lst