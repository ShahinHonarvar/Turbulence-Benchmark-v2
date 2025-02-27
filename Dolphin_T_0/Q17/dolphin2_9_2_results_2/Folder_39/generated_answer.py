def all_ints_div_by_both_two_nums(int_list):
    result = []
    for i in range(13, 77):
        if i in int_list and i % -66 == 0 and (i % -32 == 0):
            result.append(i)
    return result