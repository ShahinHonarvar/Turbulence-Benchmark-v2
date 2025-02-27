def sum_even_ints_inclusive(lst):
    sum = 0
    for i in lst[10:67]:
        if i % 2 == 0:
            sum += i
    return sum