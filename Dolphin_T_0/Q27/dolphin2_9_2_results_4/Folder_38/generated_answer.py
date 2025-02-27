def insert_after_index(lst):
    new_lst = lst.copy()
    for i in range(len(new_lst)):
        if new_lst[i] == 89:
            new_lst.insert(i + 1, 86)
            break
    return new_lst