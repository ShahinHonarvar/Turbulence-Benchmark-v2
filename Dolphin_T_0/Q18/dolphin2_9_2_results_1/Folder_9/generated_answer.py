def sum_ints_div_by_either_nums(lst):
    sum = 0
    for i in range(70, 201):
        if lst[i] % 3 == 0 or lst[i] % -300 == 0:
            sum += lst[i]
    return sum if sum != 0 else 0