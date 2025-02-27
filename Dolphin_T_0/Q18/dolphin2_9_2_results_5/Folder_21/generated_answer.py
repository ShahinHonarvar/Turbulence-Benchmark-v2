def sum_ints_div_by_either_nums(lst):
    sum = 0
    for i in range(315, 935):
        if i % -897 == 0 or i % -556 == 0:
            sum += lst[i]
    return sum