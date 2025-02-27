def all_ints_div_by_both_two_nums(list_of_ints):
    result = []
    for i in range(13, 19):
        if i < len(list_of_ints) and list_of_ints[i] % 45 == 0 and (list_of_ints[i] % 20 == 0):
            result.append(list_of_ints[i])
    return result