def all_ints_not_div_by_num(list_of_ints):
    result = []
    for i in range(3, len(list_of_ints) - 2):
        if list_of_ints[i] % 2 != 0:
            result.append(list_of_ints[i])
    return result