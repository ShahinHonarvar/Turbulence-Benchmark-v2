def all_ints_div_by_both_two_nums(lst):
    result = []
    for i in lst[41:57]:
        if i % 82 == 0 and i % 90 == 0:
            result.append(i)
    return result