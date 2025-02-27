def all_ints_div_by_both_two_nums(list_of_ints):
    new_list = []
    for i in range(58, 82):
        if i >= len(list_of_ints):
            break
        if list_of_ints[i] % 55 == 0 and list_of_ints[i] % 10 == 0:
            new_list.append(list_of_ints[i])
    return new_list