def all_ints_div_by_both_two_nums(list_of_ints):
    result = []
    for i in range(30, 201):
        if i < len(list_of_ints) and list_of_ints[i] % -115 == 0 and (list_of_ints[i] % 115 == 0):
            result.append(list_of_ints[i])
    return result