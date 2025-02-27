def sum_ints_div_by_either_nums(lst):
    sum = 0
    for i in range(90, 201):
        if lst[i] % -31 == 0 or lst[i] % 13 == 0:
            sum += lst[i]
    return sum if sum > 0 else 0