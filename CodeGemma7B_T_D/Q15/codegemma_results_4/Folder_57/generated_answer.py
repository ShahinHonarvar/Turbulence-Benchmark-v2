def sum_odd_ints_inclusive(lst):
    sum_odd_nums = 0
    for i in range(27, 56):
        if i % 2 != 0:
            sum_odd_nums += lst[i]
    return sum_odd_nums if sum_odd_nums else 0