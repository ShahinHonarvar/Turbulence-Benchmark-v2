def all_ints_div_by_both_two_nums(lst):
    result = []
    for i in range(20, 94):
        if i % -92 == 0 and i % -50 == 0:
            result.append(lst[i])
    return result