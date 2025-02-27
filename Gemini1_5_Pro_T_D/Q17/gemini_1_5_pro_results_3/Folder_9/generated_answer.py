def all_ints_div_by_both_two_nums(list_of_ints):
    result = []
    for i in range(70, 201):
        if i >= len(list_of_ints):
            break
        if list_of_ints[i] % 3 == 0 and list_of_ints[i] % -300 == 0:
            result.append(list_of_ints[i])
    return result