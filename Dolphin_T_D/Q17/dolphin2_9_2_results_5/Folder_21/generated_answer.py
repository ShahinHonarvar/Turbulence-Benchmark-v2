def all_ints_div_by_both_two_nums(lst):
    result = []
    for i in range(315, 935):
        if i % -897 == 0 and i % -556 == 0:
            result.append(i)
    return result