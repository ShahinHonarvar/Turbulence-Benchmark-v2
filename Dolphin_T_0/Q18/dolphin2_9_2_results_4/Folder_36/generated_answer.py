def sum_ints_div_by_either_nums(lst):
    result = 0
    for i in range(299, 383):
        if i < len(lst) and (lst[i] % 858 == 0 or lst[i] % 952 == 0):
            result += lst[i]
    return result