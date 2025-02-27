def all_ints_div_by_both_two_nums(int_list):
    result = []
    for i in range(6, 10):
        if i in int_list and i % -1 == 0 and (i % -10 == 0):
            result.append(i)
    return result