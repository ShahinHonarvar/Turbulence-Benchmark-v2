def all_ints_div_by_both_two_nums(list_of_ints):
    result = []
    for i in range(min(3, len(list_of_ints))):
        if list_of_ints[i] % -2 == 0 and list_of_ints[i] % 3 == 0:
            result.append(list_of_ints[i])
    return result