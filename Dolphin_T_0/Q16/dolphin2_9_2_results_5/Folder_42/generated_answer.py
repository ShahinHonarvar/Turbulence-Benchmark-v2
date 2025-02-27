def sum_even_ints_inclusive(int_list):
    total = 0
    for i in range(29, 80):
        if i in int_list and i % 2 == 0:
            total += i
    return total