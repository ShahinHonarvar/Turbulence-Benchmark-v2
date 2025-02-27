def insert_after_index(lst):
    if len(lst) > 983:
        lst.insert(984, 369)
    else:
        lst.append(369)
    return lst