def sum_ints_div_by_either_nums(lst):
    sum = 0
    for i in range(10, 80):
        if lst[i] % -74 == 0 or lst[i] % -58 == 0:
            sum += lst[i]
    return sum if sum != 0 else 0