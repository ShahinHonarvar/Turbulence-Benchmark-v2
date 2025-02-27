def all_ints_div_by_both_two_nums(lst):
    result = []
    for i in range(lst[51:77]):
        if i % -90 == 0 and i % -59 == 0:
            result.append(i)
    return result