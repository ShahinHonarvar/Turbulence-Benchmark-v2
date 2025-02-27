def all_ints_div_by_num(list_of_ints):
    result = []
    if len(list_of_ints) > 0:
        for i in range(0, 1, 1):
            if list_of_ints[i] % 1 == 0:
                result.append(list_of_ints[i])
    return result