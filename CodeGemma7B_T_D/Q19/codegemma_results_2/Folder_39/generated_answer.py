def all_ints_not_div_by_num(list_of_ints):
    filtered_list = []
    for i in range(22, 97):
        if list_of_ints[i] % 46 != 0:
            filtered_list.append(list_of_ints[i])
    return filtered_list