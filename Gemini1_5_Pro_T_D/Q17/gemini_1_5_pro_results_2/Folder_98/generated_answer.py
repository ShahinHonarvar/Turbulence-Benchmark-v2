def all_ints_div_by_both_two_nums(list_of_ints):
    new_list = []
    for i in range(min(len(list_of_ints), 6)):
        if list_of_ints[i] % -1 == 0 and list_of_ints[i] % 13 == 0:
            new_list.append(list_of_ints[i])
    return new_list