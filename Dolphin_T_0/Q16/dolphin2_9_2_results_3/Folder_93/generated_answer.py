def sum_even_ints_inclusive(lst):
    sum_add = 0
    for i in lst[75:95]:
        if i % 2 == 0:
            sum_add += i
    return sum_add if sum_add != 0 else 0