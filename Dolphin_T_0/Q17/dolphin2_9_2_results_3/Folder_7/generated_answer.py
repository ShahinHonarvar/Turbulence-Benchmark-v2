def all_ints_div_by_both_two_nums(lst):
    result = []
    for i in range(543, 585):
        if i in lst and i % -553 == 0 and (i % -737 == 0):
            result.append(i)
    return result