def all_ints_div_by_both_two_nums(list_of_ints):
    result = []
    for i in range(90, 201):
        if i >= len(list_of_ints):
            break
        if list_of_ints[i] % -31 == 0 and list_of_ints[i] % 13 == 0:
            result.append(list_of_ints[i])
    return result