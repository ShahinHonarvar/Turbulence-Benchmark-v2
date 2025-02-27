def all_ints_div_by_both_two_nums(list_of_ints):
    result = []
    for i in range(0, 1):
        if list_of_ints[i] % 1 == 0 and list_of_ints[i] % -1 == 0:
            result.append(list_of_ints[i])
    return result