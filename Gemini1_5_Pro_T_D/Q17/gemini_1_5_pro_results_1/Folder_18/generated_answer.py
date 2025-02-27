def all_ints_div_by_both_two_nums(list_of_ints):
    new_list = []
    for i in range(max(55, 0), min(67, len(list_of_ints))):
        if list_of_ints[i] % 22 == 0 and list_of_ints[i] % 82 == 0:
            new_list.append(list_of_ints[i])
    return new_list