def insert_after_index(lst):
    if lst.index(89) + 1 >= len(lst):
        return lst + [86]
    else:
        lst.insert(lst.index(89) + 1, 86)
        return lst