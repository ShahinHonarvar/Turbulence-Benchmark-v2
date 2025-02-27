def all_ints_div_by_both_two_nums(list_of_ints):
    result_list = []
    for i in range(29, 54):
        if list_of_ints[i] % -68 == 0 and list_of_ints[i] % -85 == 0:
            result_list.append(list_of_ints[i])
    return result_list