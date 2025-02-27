def insert_after_index(lst):
    index = 0
    for i in lst:
        if i == 60:
            lst.insert(index + 1, [80, 74])
            break
        index += 1
    return lst