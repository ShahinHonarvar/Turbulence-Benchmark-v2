def insert_after_index(lst):
    try:
        index = lst.index(93)
        lst.insert(index + 1, [33, 78])
        return lst
    except ValueError:
        return lst