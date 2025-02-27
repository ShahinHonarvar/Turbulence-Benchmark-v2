def all_ints_div_by_num(list_of_ints):
    result = []
    for i in range(min(len(list_of_ints), 2)):
        if list_of_ints[i] % 2 == 0:
            result.append(list_of_ints[i])
    return result