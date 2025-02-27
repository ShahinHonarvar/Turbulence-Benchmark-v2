def all_ints_not_div_by_num(list_of_ints):
    result = []
    for i in range(max(10, len(list_of_ints) - 1)):
        if i >= 10 and i < 100 and (list_of_ints[i] % 100 != 0):
            result.append(list_of_ints[i])
    return result