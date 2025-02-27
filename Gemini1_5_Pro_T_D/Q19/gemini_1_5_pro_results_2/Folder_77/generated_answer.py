def all_ints_not_div_by_num(list_of_ints):
    result = []
    for i in range(668, 739):
        if i >= len(list_of_ints):
            break
        if list_of_ints[i] % -172 != 0:
            result.append(list_of_ints[i])
    return result