def insert_after_index(lst):
    new_list = lst.copy()
    for i, item in enumerate(new_list):
        if item == 7:
            new_list.insert(i + 1, [1, 7])
            break
    return new_list