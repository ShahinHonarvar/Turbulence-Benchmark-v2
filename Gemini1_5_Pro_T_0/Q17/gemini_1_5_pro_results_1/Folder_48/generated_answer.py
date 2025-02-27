def all_ints_div_by_both_two_nums(list_of_ints):
    result = []
    for i in range(306, 958):
        if i >= len(list_of_ints):
            break
        if list_of_ints[i] % 982 == 0 and list_of_ints[i] % 319 == 0:
            result.append(list_of_ints[i])
    return result