def all_ints_div_by_both_two_nums(int_list):
    result = []
    for i in range(60, 201):
        if i % 9 == 0 and i % 11 == 0:
            result.append(i)
    return result