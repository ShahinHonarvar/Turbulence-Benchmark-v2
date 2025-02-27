def all_pos_ints_exclusive(list1):
    new_list = []
    for i in range(21, 51):
        if i < len(list1) and list1[i] > 0:
            new_list.append(list1[i])
    return new_list