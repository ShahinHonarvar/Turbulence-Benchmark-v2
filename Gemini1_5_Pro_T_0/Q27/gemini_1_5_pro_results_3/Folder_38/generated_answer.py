def insert_after_index(list_in):
    for i in range(len(list_in)):
        if list_in[i] == 89:
            list_in.insert(i + 1, 86)
            break
    return list_in