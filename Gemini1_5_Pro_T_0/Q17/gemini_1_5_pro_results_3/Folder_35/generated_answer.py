def all_ints_div_by_both_two_nums(list_of_ints):
    result = []
    for i in range(max(77, 0), min(len(list_of_ints), 88)):
        if list_of_ints[i] % 23 == 0 and list_of_ints[i] % 57 == 0:
            result.append(list_of_ints[i])
    return result