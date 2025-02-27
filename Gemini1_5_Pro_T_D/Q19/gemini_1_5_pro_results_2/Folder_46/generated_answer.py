def all_ints_not_div_by_num(list1):
    new_list = []
    for i in range(19, 59):
        if i < len(list1) and list1[i] % 86 != 0:
            new_list.append(list1[i])
    return new_list