def all_ints_div_by_both_two_nums(ls):
    result = []
    for i in range(11, 47):
        if ls[i] % 55 == 0 and ls[i] % 36 == 0:
            result.append(ls[i])
    return result