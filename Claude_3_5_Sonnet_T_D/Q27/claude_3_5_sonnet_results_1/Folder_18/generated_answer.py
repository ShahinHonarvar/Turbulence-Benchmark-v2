def insert_after_index(lst):
    index = 696
    if index + 1 <= len(lst):
        lst.insert(index + 1, 477)
    else:
        lst.append(477)
    return lst