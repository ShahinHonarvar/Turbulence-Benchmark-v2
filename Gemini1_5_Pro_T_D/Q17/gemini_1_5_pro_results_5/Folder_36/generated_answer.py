def all_ints_div_by_both_two_nums(list_of_ints):
    result = []
    for i in range(299, 383):
        if i >= len(list_of_ints):
            break
        if list_of_ints[i] % 858 == 0 and list_of_ints[i] % 952 == 0:
            result.append(list_of_ints[i])
    return result