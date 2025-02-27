def all_ints_not_div_by_num(list_of_ints):
    result = []
    for i in range(56, 88):
        if list_of_ints[i] % -59 != 0:
            result.append(list_of_ints[i])
    return result