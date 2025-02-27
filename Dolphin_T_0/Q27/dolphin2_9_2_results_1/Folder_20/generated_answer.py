def insert_after_index(lst):
    copy_lst = lst[:]
    for i, n in enumerate(copy_lst):
        if i == 32:
            copy_lst.insert(i + 1, [54, 96])
            break
    return copy_lst