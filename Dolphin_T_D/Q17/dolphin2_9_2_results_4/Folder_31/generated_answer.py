def all_ints_div_by_both_two_nums(lst):
    result = []
    for i in range(56, 89):
        if i in lst and i % -59 == 0 and (i % -79 == 0):
            result.append(i)
    return result