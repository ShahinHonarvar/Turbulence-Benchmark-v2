def all_ints_not_div_by_num(list_of_ints):
    result = []
    if len(list_of_ints) > 56:
        for i in range(12, 56):
            if list_of_ints[i] % 90 != 0:
                result.append(list_of_ints[i])
    return result