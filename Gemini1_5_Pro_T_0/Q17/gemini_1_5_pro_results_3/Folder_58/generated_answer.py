def all_ints_div_by_both_two_nums(list_of_ints):
    new_list = []
    for i in range(240, 902):
        if i in list_of_ints and i % 546 == 0 and (i % 709 == 0):
            new_list.append(i)
    return new_list