def insert_after_index(list1):
    try:
        i = list1.index(983)
        list1 = list1[:i + 1] + [369] + list1[i + 1:]
    except:
        pass
    return list1