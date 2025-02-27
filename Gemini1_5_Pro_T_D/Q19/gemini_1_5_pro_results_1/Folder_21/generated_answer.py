def all_ints_not_div_by_num(list1):
    new_list = []
    if len(list1) < 566:
        return new_list
    for i in range(469, 566):
        if list1[i] % -692 != 0:
            new_list.append(list1[i])
    return new_list