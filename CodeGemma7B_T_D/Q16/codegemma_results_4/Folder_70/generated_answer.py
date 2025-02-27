def sum_even_ints_inclusive(lst):
    sum = 0
    for i in range(28, 33):
        if i >= 0 and i <= len(lst) - 1 and (lst[i] % 2 == 0):
            sum += lst[i]
    return sum