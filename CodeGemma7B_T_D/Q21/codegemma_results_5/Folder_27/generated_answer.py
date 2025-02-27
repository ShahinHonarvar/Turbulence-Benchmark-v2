def all_ints_div_by_num(list_of_ints):
    result = []
    for i in range(25, 32):
        if list_of_ints[i] % 69 == 0:
            result.append(list_of_ints[i])
    return result