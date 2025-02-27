def insert_after_index(lst):
    for i, item in enumerate(lst):
        if item == 66 and i < len(lst) - 1 and (lst[i + 1] != 45):
            lst.insert(i + 2, 45)
            break
    return lst