def all_ints_div_by_both_two_nums(list_of_ints):
    filtered_list = []
    for i in range(57, 85):
        if i >= len(list_of_ints):
            break
        if list_of_ints[i] % -30 == 0 and list_of_ints[i] % -88 == 0:
            filtered_list.append(list_of_ints[i])
    return filtered_list