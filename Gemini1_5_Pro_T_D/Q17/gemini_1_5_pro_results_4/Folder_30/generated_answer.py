def all_ints_div_by_both_two_nums(list_of_ints):
    result = []
    for i in range(max(11, 0), min(77, len(list_of_ints))):
        if list_of_ints[i] % -81 == 0 and list_of_ints[i] % -94 == 0:
            result.append(list_of_ints[i])
    return result