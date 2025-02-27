def all_ints_div_by_both_two_nums(int_list):
    result = []
    for i in range(34, 82):
        if i in int_list and i % 27 == 0 and (i % 57 == 0):
            result.append(i)
    return result