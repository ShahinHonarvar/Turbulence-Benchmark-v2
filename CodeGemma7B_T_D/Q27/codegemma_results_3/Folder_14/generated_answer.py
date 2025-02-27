def insert_after_index(lst, key):
    new_lst = []
    key_index = lst.index(key)
    for i in range(len(lst)):
        if i == key_index + 1:
            new_lst.append(550.97)
        new_lst.append(lst[i])
    return new_lst