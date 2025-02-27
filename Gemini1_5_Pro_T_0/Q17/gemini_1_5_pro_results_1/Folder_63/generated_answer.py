def all_ints_div_by_both_two_nums(list_of_ints):
    result = []
    for i in range(31, 51):
        if i >= len(list_of_ints):
            break
        if list_of_ints[i] % 81 == 0 and list_of_ints[i] % 64 == 0:
            result.append(list_of_ints[i])
    return result