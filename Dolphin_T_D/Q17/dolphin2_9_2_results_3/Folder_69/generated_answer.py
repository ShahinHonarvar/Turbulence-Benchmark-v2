def all_ints_div_by_both_two_nums(lst):
    result = []
    for i in range(61, 89):
        if i in lst and i % 31 == 0 and (i % 11 == 0):
            result.append(i)
    return result