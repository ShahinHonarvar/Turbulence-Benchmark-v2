def insert_after_index(lst):
    idx = lst.index(89)
    if idx == len(lst) - 1:
        lst.append(86)
    else:
        lst.insert(idx + 1, 86)
    return lst