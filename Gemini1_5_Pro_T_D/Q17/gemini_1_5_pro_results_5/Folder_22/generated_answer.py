def all_ints_div_by_both_two_nums(list_of_ints):
    new_list = []
    for i in range(40, 201):
        if i in list_of_ints and i % 21 == 0 and (i % 71 == 0):
            new_list.append(i)
    return new_list