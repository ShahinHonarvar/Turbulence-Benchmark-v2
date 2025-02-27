def all_ints_div_by_both_two_nums(int_list):
    result = []
    for i in range(44, 60):
        if i in int_list and i % 39 == 0 and (i % 15 == 0):
            result.append(i)
    return result