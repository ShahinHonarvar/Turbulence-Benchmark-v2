def all_ints_not_div_by_num(list1):
    new_list = []
    for i in range(4, 9):
        if i < len(list1):
            if list1[i] % 6 != 0:
                new_list.append(list1[i])
    return new_list