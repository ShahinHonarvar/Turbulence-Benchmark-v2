def insert_after_index(lst):
    new_lst = lst[:]
    for i, item in enumerate(new_lst):
        if item == 35:
            new_lst[i + 1:i + 1] = [90, 76]
            break
    return new_lst