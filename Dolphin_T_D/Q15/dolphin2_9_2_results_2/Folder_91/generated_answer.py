def sum_odd_ints_inclusive(lst):
    sum = 0
    for i in range(len(lst) + 1):
        if i > 0 and i <= 5 and (lst[i - 1] % 2 != 0):
            sum += lst[i - 1]
    return sum