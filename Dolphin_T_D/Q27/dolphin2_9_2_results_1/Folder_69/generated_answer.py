def insert_after_index(lst):
    indices = [i for i, val in enumerate(lst) if val == 564]
    if indices:
        index = indices[0]
        if index + 1 < len(lst):
            lst.insert(index + 1, 149)
    else:
        index = None
    return lst if index else 'Index 564 not found'