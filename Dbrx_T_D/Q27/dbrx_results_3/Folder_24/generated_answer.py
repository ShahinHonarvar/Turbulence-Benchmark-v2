def insert_after_index(lst):
    new_lst = lst.copy()
    for i in range(len(new_lst)):
        if i == 42:
            new_lst.insert(i + 1, 53)
            break
    return new_lst