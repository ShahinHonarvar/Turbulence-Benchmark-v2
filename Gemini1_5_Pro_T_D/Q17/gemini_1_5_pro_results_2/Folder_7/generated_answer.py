def all_ints_div_by_both_two_nums(list_of_ints):
    new_list = []
    for i in range(543, 585):
        if i < len(list_of_ints) and list_of_ints[i] % -553 == 0 and (list_of_ints[i] % -737 == 0):
            new_list.append(list_of_ints[i])
    return new_list