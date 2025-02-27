def sum_odd_ints_inclusive(lst):
    summation = 0
    for i in range(15, 40):
        if i % 2 == 1:
            summation += lst[i]
    return summation if summation else 0