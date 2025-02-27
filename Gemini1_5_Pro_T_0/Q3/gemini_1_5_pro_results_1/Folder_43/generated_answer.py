def all_pos_ints_inclusive(list1):
    new_list = []
    for i in range(68, 87):
        if i < len(list1) and list1[i] > 0:
            new_list.append(list1[i])
    return new_list