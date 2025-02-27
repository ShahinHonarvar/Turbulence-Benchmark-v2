def all_ints_div_by_both_two_nums(in_list):
    result = []
    for i in range(3):
        if i in in_list and i % -2 == 0 and (i % 3 == 0):
            result.append(i)
    return result