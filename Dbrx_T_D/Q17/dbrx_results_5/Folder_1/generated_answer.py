def all_ints_div_by_both_two_nums(list_of_ints):
    result = []
    for i in range(10, 29):
        if list_of_ints[i] % -61 == 0 and list_of_ints[i] % -64 == 0:
            result.append(list_of_ints[i])
    return result