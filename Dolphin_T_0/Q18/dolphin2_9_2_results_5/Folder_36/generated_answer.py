def sum_ints_div_by_either_nums(lst):
    sum = 0
    for i in range(299, 383):
        if i in lst and (lst[i] % 858 == 0 or lst[i] % 952 == 0):
            sum += lst[i]
    return sum