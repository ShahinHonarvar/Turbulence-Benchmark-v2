def insert_after_index(lst):
    new_list = lst.copy()
    try:
        index = lst.index(99)
        new_list.insert(index + 1, 15)
    except ValueError:
        new_list.append(15)
    return new_list