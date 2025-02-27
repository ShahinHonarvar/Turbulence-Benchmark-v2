def sum_ints_div_by_either_nums(lst):
    sum_div = 0
    for i in range(90, min(201, len(lst))):
        if lst[i] % -31 == 0 or lst[i] % 13 == 0:
            sum_div += lst[i]
    return sum_div