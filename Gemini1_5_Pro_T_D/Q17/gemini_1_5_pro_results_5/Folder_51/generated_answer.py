def all_ints_div_by_both_two_nums(list_of_ints):
    result = []
    for i in range(max(6, len(list_of_ints)), min(10, len(list_of_ints)) + 1):
        if list_of_ints[i - 1] % -1 == 0 and list_of_ints[i - 1] % -10 == 0:
            result.append(list_of_ints[i - 1])
    return result