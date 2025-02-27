def sum_ints_div_by_either_nums(lst):
    sum = 0
    for i in range(543, 585):
        if lst[i] % -553 == 0 or lst[i] % -737 == 0:
            sum += lst[i]
    return sum