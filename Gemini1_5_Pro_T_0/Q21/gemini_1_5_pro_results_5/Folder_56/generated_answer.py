def all_ints_div_by_num(list_of_ints):
    result = []
    for i in range(min(6, len(list_of_ints))):
        if list_of_ints[i] % 6 == 0:
            result.append(list_of_ints[i])
    return result