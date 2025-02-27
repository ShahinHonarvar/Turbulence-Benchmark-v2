def sum_even_ints_inclusive(lst):
    sum = 0
    for x in lst:
        if x % 2 == 0:
            sum += x
    return sum