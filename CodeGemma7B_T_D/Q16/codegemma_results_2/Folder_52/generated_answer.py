def sum_even_ints_inclusive(int_list):
    summ = 0
    for i in int_list[28:39]:
        if i % 2 == 0:
            summ += i
    if summ == 0:
        return 0
    return summ