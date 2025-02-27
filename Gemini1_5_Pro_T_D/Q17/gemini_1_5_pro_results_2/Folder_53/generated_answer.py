def all_ints_div_by_both_two_nums(list_of_ints):
    new_list = []
    for i in range(200, 201):
        try:
            if list_of_ints[i] % 17 == 0 and list_of_ints[i] % -5 == 0:
                new_list.append(list_of_ints[i])
        except:
            continue
    return new_list