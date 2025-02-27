def all_ints_div_by_both_two_nums(lst):
    result = []
    for i in range(13, 76 + 1):
        if i % -66 == 0 and i % -32 == 0:
            result.append(lst[i])
    return result