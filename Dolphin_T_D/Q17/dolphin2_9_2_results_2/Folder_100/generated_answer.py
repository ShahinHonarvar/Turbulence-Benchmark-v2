def all_ints_div_by_both_two_nums(lst):
    result = []
    for i in lst[72:94]:
        if i % 32 == 0 and i % 44 == 0:
            result.append(i)
    return result