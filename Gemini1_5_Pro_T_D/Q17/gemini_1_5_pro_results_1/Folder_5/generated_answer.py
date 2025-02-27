def all_ints_div_by_both_two_nums(list_of_ints):
    result = []
    for i in range(min(len(list_of_ints), 2)):
        if list_of_ints[i] % -6 == 0 and list_of_ints[i] % 4 == 0:
            result.append(list_of_ints[i])
    return result