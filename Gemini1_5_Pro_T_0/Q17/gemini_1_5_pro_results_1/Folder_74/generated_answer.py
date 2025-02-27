def all_ints_div_by_both_two_nums(list_of_ints):
    result = []
    for i in range(max(90, 0), min(len(list_of_ints), 98)):
        if list_of_ints[i] % 13 == 0 and list_of_ints[i] % 35 == 0:
            result.append(list_of_ints[i])
    return result