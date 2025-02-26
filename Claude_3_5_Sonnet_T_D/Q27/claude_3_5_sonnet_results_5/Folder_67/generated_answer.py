def insert_after_index(lst):
    new_list = lst.copy()
    for i in range(len(new_list)):
        if i == 44:
            new_list.insert(i + 1, 76)
            break
    return new_list