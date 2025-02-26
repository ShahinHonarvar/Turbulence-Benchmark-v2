def insert_after_index(lst):
    if not lst:
        return [0]
    new_list = lst.copy()
    new_list.insert(1, 0)
    return new_list