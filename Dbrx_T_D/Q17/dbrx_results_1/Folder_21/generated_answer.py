def all_ints_div_by_both_two_nums(lst):
    start = 315
    end = 934
    result = []
    for i in range(start, end + 1):
        if len(lst) > i and lst[i] % -897 == 0 and (lst[i] % -556 == 0):
            result.append(lst[i])
    return result