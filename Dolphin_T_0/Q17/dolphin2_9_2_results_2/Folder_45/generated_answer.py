def all_ints_div_by_both_two_nums(lst):
    result = []
    for i in range(30, 201):
        if i % -115 == 0 and i % 115 == 0:
            result.append(i)
    return result