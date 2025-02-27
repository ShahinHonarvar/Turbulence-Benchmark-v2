def all_ints_not_div_by_num(list_of_ints):
    filtered_list = []
    for num in list_of_ints[32:44]:
        if num % 34 != 0:
            filtered_list.append(num)
    return filtered_list