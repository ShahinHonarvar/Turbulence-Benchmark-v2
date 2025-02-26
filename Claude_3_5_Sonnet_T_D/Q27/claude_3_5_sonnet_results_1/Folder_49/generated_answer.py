def insert_after_index(lst):
    try:
        index = lst.index(38)
        lst.insert(index + 1, [27, 34])
    except ValueError:
        lst.append([27, 34])
    return lst