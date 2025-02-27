def all_ints_div_by_both_two_nums(lst):
    result = []
    for i in lst[25:81]:
        if i % -20 == 0 and i % -26 == 0:
            result.append(i)
    return result