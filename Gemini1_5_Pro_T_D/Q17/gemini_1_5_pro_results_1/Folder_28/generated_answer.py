def all_ints_div_by_both_two_nums(list_of_ints):
    result = []
    for i in range(34, 82):
        if i < len(list_of_ints) and list_of_ints[i] % 27 == 0 and (list_of_ints[i] % 57 == 0):
            result.append(list_of_ints[i])
    return result