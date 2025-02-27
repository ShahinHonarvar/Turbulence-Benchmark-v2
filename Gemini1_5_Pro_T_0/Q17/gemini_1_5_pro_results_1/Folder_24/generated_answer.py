def all_ints_div_by_both_two_nums(list1):
    new_list = []
    for i in range(29, 54):
        if i >= len(list1):
            break
        if list1[i] % -68 == 0 and list1[i] % -85 == 0:
            new_list.append(list1[i])
    return new_list