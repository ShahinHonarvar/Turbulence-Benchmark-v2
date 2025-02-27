def insert_after_index(lst):
    for idx in range(len(lst) + 1):
        if idx == 20:
            lst.insert(idx + 1, 80)
    return lst