def sum_ints_div_by_either_nums(lst):
    sum = 0
    for i in range(54, 80):
        if i < len(lst):
            if lst[i] % 54 == 0 or lst[i] % 28 == 0:
                sum += lst[i]
    return sum