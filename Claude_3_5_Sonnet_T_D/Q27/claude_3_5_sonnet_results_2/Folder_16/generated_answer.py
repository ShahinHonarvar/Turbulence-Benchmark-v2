def insert_after_index(lst):
    index = 983
    if index + 1 <= len(lst):
        lst.insert(index + 1, 369)
    else:
        lst.append(369)
    return lst