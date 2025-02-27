def all_ints_not_div_by_num(list_of_ints):
    result = []
    for i in range(31, 69):
        if list_of_ints[i] % -70 != 0:
            result.append(list_of_ints[i])
    return result