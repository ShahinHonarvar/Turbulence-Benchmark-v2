def all_ints_div_by_both_two_nums(lst):
    result = []
    for x in lst[:6]:
        if x % -1 == 0 and x % 13 == 0:
            result.append(x)
    return result