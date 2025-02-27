def sum_odd_ints_inclusive(lst):
    sum = 0
    for i in range(70, 85):
        if i >= 0 and i < len(lst) and (lst[i] % 2 != 0):
            sum += lst[i]
    return sum