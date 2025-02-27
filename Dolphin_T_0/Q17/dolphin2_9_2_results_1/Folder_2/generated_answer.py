def all_ints_div_by_both_two_nums(lst):
    result = []
    for i in lst[73:87]:
        if i % 54 == 0 and i % 82 == 0:
            result.append(i)
    return result