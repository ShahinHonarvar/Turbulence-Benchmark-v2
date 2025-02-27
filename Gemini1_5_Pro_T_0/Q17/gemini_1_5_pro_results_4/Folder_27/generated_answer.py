def all_ints_div_by_both_two_nums(list_of_ints):
    result = []
    for i in range(20, 36):
        if i >= len(list_of_ints):
            break
        if list_of_ints[i] % -36 == 0 and list_of_ints[i] % -89 == 0:
            result.append(list_of_ints[i])
    return result