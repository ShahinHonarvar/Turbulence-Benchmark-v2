def all_pos_ints_exclusive(list1):
    new_list = []
    for i in range(743, 867):
        if i in range(len(list1)):
            if list1[i] > 0:
                new_list.append(list1[i])
    return new_list