def sum_even_ints_inclusive(lst):
    total = 0
    for i in lst[28:41]:
        if i % 2 == 0:
            total += i
    return total