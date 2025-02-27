def sum_ints_div_by_either_nums(list):
    sum = 0
    for i in range(7, 10):
        if list[i] % 2 == 0 or list[i] % 3 == 0:
            sum = sum + list[i]
    return sum