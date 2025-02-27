def all_ints_not_div_by_num(list_of_ints):
    result = []
    for i in range(max(10, 0), min(100, len(list_of_ints) - 1)):
        if list_of_ints[i] % 100 != 0:
            result.append(list_of_ints[i])
    return result