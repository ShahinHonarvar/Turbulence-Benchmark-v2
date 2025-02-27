def insert_after_index(list):
    index = 0
    for element in list:
        if element == 412:
            index = list.index(412) + 1
    list.insert(index, 668)
    return list