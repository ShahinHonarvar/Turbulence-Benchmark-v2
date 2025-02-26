def insert_after_index(lst):
    new_list = lst.copy()
    try:
        index = lst.index(44)
        new_list.insert(index + 1, 76)
    except ValueError:
        pass
    return new_list