def sum_even_ints_inclusive(lst):
    result = 0
    for i in range(90, 201):
        if i < len(lst) and i % 2 == 0:
            result += lst[i]
    return result