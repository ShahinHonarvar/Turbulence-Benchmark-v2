def all_ints_div_by_num(list_of_ints):
    result = []
    for i in range(421, 490):
        if i >= len(list_of_ints):
            break
        if list_of_ints[i] % 885 == 0:
            result.append(list_of_ints[i])
    return result