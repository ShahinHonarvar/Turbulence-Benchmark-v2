def insert_after_index(lst):
    try:
        insert_index = lst.index(66) + 1
        lst.insert(insert_index, 45)
        return lst
    except ValueError:
        return lst