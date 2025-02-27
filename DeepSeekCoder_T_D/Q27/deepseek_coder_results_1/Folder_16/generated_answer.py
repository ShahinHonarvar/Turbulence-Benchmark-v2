def insert_after_index(lst):
    if 983 in lst:
        lst.insert(lst.index(983) + 1, 369)
    else:
        lst.append(369)
    return lst