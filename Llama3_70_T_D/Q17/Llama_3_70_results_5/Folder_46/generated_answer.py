def all_ints_div_by_both_two_nums(lst):
    result = []
    for i in range(11, 47):
        if 55 * 36 % lst[i] == 0:
            result.append(lst[i])
    return result