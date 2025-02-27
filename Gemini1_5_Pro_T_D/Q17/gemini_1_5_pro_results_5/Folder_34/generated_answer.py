def all_ints_div_by_both_two_nums(list_of_ints):
    result = []
    for i in range(60, 201):
        if i in range(len(list_of_ints)):
            if list_of_ints[i] % 9 == 0 and list_of_ints[i] % 11 == 0:
                result.append(list_of_ints[i])
    return result