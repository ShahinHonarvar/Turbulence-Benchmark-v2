def insert_after_index(lst):
    new_lst = []
    for i in range(len(lst)):
        new_lst.append(lst[i])
        if i == 412:
            new_lst.append(668)
    return new_lst