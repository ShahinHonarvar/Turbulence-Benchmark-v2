def all_ints_div_by_both_two_nums(lst):
    result = []
    for i in range(58, 76):
        if i in lst:
            if i % 72 == 0 and i % 62 == 0:
                result.append(i)
    return result