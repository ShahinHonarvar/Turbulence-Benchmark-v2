def insert_after_index(lst):
    try:
        i = lst.index(70) + 1
        lst.insert(i, 76)
        return lst
    except:
        return lst