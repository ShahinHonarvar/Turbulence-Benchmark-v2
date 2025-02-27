def sum_even_ints_inclusive(int_list):
    total = 0
    for i in int_list[28:41]:
        if i % 2 == 0:
            total += i
    return total or 0