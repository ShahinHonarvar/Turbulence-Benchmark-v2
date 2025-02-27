def sum_ints_div_by_either_nums(lst):
    sum_of_divs = 0
    for i in range(40, 201):
        if lst[i] % 21 == 0 or lst[i] % 71 == 0:
            sum_of_divs += lst[i]
    return sum_of_divs