def all_ints_div_by_both_two_nums(lst):
    result = []
    for i in lst[35:65]:
        if i % -30 == 0 and i % -95 == 0:
            result.append(i)
    return result