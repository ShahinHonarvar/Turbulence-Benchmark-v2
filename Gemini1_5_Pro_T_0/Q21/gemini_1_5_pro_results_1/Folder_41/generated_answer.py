def all_ints_div_by_num(list_of_ints):
    new_list = []
    for i in range(6):
        if i < len(list_of_ints) and list_of_ints[i] % 5 == 0:
            new_list.append(list_of_ints[i])
    return new_list