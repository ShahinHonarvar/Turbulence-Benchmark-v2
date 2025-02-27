def sum_ints_div_by_either_nums(lst):
    sum_integers = 0
    for i in range(20, 36):
        if i % -36 == 0 or i % -89 == 0:
            sum_integers += lst[i]
    return sum_integers if sum_integers > 0 else 0