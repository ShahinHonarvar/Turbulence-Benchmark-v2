def insert_after_index(list_in):
    try:
        i = list_in.index(983)
        list_in.insert(i + 1, 369)
        return list_in
    except:
        return list_in