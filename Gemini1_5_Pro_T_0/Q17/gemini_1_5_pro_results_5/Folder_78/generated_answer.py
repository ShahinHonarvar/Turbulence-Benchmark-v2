def all_ints_div_by_both_two_nums(list_of_ints):
    result = []
    for i in range(34, 70):
        if i >= len(list_of_ints):
            break
        if list_of_ints[i] % 19 == 0 and list_of_ints[i] % 32 == 0:
            result.append(list_of_ints[i])
    return result