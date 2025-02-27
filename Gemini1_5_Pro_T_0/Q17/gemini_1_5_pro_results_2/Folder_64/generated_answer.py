def all_ints_div_by_both_two_nums(list_of_ints):
    result = []
    for i in range(0, 4):
        if i >= len(list_of_ints):
            break
        if list_of_ints[i] % 11 == 0 and list_of_ints[i] % -7 == 0:
            result.append(list_of_ints[i])
    return result