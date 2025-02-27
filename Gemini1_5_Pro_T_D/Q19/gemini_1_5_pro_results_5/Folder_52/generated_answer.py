def all_ints_not_div_by_num(list_of_ints):
    result = []
    for i in range(50, 92):
        if i >= len(list_of_ints):
            break
        if list_of_ints[i] % 16 != 0:
            result.append(list_of_ints[i])
    return result