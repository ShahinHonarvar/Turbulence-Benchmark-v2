def all_ints_div_by_both_two_nums(list_of_ints):
    new_list = []
    for i in range(min(10, len(list_of_ints))):
        if list_of_ints[i] % 10 == 0 and list_of_ints[i] % 100 == 0:
            new_list.append(list_of_ints[i])
    return new_list