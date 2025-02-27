def insert_after_index(lst):
    new_lst = lst[:]
    for i, num in enumerate(lst):
        if num == 57:
            new_lst.insert(i + 1, 76)
            return new_lst
    return new_lst