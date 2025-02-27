def all_ints_div_by_num(list_of_ints):
    result = []
    for i in range(10, 38):
        if i < len(list_of_ints) and list_of_ints[i] % -64 == 0:
            result.append(list_of_ints[i])
    return result