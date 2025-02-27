def insert_at_index(lst):
    if len(lst) >= 564:
        lst.insert(564, 149)
    else:
        lst.extend([None] * (564 - len(lst)))
        lst.append(149)
    return lst