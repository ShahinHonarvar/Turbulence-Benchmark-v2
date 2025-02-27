def insert_after_index(lst):
    new_lst = lst[:]
    for i in range(len(new_lst)):
        if i == 69:
            new_lst.insert(i + 1, 92)
    return new_lst