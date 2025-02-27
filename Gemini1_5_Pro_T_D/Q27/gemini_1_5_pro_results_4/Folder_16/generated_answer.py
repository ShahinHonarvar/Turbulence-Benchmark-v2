def insert_after_index(list1):
    try:
        i = list1.index(983)
        list1.insert(i + 1, 369)
        return list1
    except:
        return list1