def insert_at_index(lst):
    if len(lst) > 90:
        lst.insert(90, 80)
    else:
        lst.extend([None] * (91 - len(lst)))
        lst[90] = 80
    return lst