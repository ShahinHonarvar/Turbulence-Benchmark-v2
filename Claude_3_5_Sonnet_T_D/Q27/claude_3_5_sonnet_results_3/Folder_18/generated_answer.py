def insert_after_index(lst):
    try:
        index = lst.index(696)
        lst.insert(index + 1, 477)
    except ValueError:
        lst.append(477)
    return lst