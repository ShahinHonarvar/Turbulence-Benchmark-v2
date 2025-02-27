def sum_even_ints_inclusive(lst):
    result = 0
    for i in range(len(lst)):
        if i >= 0 and i <= 8 and (lst[i] % 2 == 0):
            result += lst[i]
    return result