def sum_ints_div_by_either_nums(lst):
    sum = 0
    for i in range(10):
        if lst[i] % 10 == 0 or lst[i] % 100 == 0:
            sum += lst[i]
    return sum if sum != 0 else None