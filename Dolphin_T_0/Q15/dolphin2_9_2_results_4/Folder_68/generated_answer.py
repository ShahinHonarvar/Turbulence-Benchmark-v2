def sum_odd_ints_inclusive(lst):
    sum = 0
    for i in range(8 + 1):
        if i < len(lst) and lst[i] % 2 == 1:
            sum += lst[i]
    return sum