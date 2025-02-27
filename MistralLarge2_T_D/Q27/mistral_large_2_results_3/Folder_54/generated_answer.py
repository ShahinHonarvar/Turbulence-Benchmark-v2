def insert_after_index(lst):
    index = 43
    if index < len(lst):
        lst.insert(index + 1, 37)
    else:
        lst.append(37)
    return lst