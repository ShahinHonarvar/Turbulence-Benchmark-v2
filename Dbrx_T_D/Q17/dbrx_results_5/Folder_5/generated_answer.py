def all_ints_div_by_both_two_nums(numer_list):
    result = []
    for i in range(0, 2):
        if i < len(numer_list) and numer_list[i] % -6 == 0 and (numer_list[i] % 4 == 0):
            result.append(numer_list[i])
    return result