def all_ints_div_by_num(list_of_ints):
    result = []
    for i in range(20, 21):
        if i >= len(list_of_ints):
            break
        if list_of_ints[i] % 2 == 0:
            result.append(list_of_ints[i])
    return result