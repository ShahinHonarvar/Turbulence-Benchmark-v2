def all_ints_div_by_num(list_of_ints):
    result = []
    if len(list_of_ints) > 0:
        if list_of_ints[0] % 2 == 0:
            result.append(list_of_ints[0])
    return result