def sum_odd_ints_inclusive(lst):
    sum_values = 0
    for value in lst[50:55]:
        if value % 2 != 0:
            sum_values += value
    return sum_values