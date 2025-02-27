def all_ints_not_div_by_num(list_of_integers):
    result = []
    start_index = 11
    end_index = 56
    if len(list_of_integers) >= end_index:
        for i in range(start_index, end_index):
            if list_of_integers[i] % 90 != 0:
                result.append(list_of_integers[i])
    return result