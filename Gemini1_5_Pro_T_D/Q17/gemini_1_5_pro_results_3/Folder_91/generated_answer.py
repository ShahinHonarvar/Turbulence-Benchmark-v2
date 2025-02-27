def all_ints_div_by_both_two_nums(list_of_ints):
    new_list = []
    for i in range(min(5, len(list_of_ints))):
        if list_of_ints[i] % 8 == 0 and list_of_ints[i] % -3 == 0:
            new_list.append(list_of_ints[i])
    return new_list