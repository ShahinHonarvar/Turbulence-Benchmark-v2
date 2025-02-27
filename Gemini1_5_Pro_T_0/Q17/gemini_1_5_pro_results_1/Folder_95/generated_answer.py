def all_ints_div_by_both_two_nums(list_of_integers):
    filtered_list = []
    for i in range(max(57, 0), min(85, len(list_of_integers))):
        if list_of_integers[i] % -30 == 0 and list_of_integers[i] % -88 == 0:
            filtered_list.append(list_of_integers[i])
    return filtered_list