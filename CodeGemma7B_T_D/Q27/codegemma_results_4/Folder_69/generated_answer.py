def insert_after_index(list):
    new_list = []
    for i in range(len(list)):
        if i == 564:
            new_list.append(list[i])
            new_list.append(149)
        else:
            new_list.append(list[i])
    return new_list