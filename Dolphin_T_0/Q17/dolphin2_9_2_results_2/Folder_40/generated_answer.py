def all_ints_div_by_both_two_nums(lst):
    result = []
    for i in range(0, 2):
        if i % 2 == 0 and i % 1 == 0:
            result.append(i)
    return result