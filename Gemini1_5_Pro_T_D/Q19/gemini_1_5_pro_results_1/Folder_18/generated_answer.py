def all_ints_not_div_by_num(list_of_integers):
    result = []
    start_index = 35
    end_index = 98
    for i in range(start_index, end_index):
        if i < len(list_of_integers) and list_of_integers[i] % 41 != 0:
            result.append(list_of_integers[i])
    return result