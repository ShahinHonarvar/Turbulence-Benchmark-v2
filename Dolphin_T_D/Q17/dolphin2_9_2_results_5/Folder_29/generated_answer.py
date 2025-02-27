def all_ints_div_by_both_two_nums(lst):
    result = []
    for i in range(55, 85):
        if i in lst:
            if i % -24 == 0 and i % -11 == 0:
                result.append(i)
    return result