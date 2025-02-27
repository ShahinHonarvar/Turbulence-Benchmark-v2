def all_ints_div_by_both_two_nums(list_of_ints):
    result = []
    for i in range(61, 89):
        if i >= len(list_of_ints):
            break
        if list_of_ints[i] % 31 == 0 and list_of_ints[i] % 11 == 0:
            result.append(list_of_ints[i])
    return result