def all_ints_not_div_by_num(list_of_ints):
    result = []
    for i in range(82, 86):
        if i < len(list_of_ints) and list_of_ints[i] % 77 != 0:
            result.append(list_of_ints[i])
    return result