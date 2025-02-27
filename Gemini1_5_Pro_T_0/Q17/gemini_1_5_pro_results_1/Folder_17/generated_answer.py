def all_ints_div_by_both_two_nums(list_of_ints):
    result = []
    for i in range(81, 90):
        if i >= len(list_of_ints):
            break
        if list_of_ints[i] % 56 == 0 and list_of_ints[i] % 68 == 0:
            result.append(list_of_ints[i])
    return result