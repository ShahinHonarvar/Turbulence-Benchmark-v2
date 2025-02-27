def sum_even_ints_inclusive(lst):
    result = 0
    for i in range(0, 11):
        if i % 2 == 0 and i % len(lst) != 0 and (i < len(lst)):
            result += lst[i]
    return result