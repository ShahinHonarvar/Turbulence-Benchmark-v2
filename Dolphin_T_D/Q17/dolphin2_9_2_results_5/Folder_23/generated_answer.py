def all_ints_div_by_both_two_nums(lst):
    result = []
    for i in lst[69:98]:
        if i % -90 == 0 and i % -67 == 0:
            result.append(i)
    return result