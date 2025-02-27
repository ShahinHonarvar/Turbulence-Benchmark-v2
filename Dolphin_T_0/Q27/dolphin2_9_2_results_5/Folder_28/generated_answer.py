def insert_after_index(lst):
    new_list = lst[:]
    for i, item in enumerate(lst):
        if item == 74:
            new_list.insert(i + 1, 49)
            return new_list
    return new_list