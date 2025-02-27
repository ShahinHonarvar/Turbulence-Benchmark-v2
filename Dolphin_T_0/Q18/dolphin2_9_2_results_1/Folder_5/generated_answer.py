def sum_ints_div_by_either_nums(lst):
    result = 0
    for i in range(0, 2):
        if i % -6 == 0 or i % 4 == 0:
            result += lst[i]
    return result if result != 0 else 0