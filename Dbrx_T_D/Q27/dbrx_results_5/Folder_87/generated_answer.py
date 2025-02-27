def insert_after_index(lst):
    index = 0
    for i in lst:
        if index == 69:
            lst.insert(index + 1, 92)
            break
        index += 1
    return lst