def sum_even_ints_inclusive(lst):
    sum = 0
    for i in range(60, 201):
        if i % 2 == 0 and i < len(lst):
            sum += lst[i]
    return sum