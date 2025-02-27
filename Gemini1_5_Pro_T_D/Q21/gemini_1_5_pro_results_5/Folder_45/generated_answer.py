def all_ints_div_by_num(list1):
    new_list = []
    for i in range(0, 3):
        if i >= len(list1):
            break
        if list1[i] % 9 == 0:
            new_list.append(list1[i])
    return new_list