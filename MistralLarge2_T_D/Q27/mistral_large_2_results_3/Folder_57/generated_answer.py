def insert_after_index(lst):
    if len(lst) > 90:
        lst.insert(91, 80)
    else:
        lst.append(80)
    return lst