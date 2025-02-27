def insert_after_index(lst):
    new_lst = lst[:]
    for i, num in enumerate(new_lst):
        if num == 90:
            new_lst.insert(i + 1, 80)
            break
    return new_lst