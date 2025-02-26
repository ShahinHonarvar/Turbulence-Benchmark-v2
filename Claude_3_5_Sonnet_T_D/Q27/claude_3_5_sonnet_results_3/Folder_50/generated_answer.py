def insert_after_index(lst):
    target_index = lst.index(52) if 52 in lst else -1
    if target_index != -1:
        lst.insert(target_index + 1, 38)
    return lst