def sum_even_ints_inclusive(int_list):
    total = 0
    int_list = int_list[40:42]
    for value in int_list:
        if value % 2 == 0:
            total += value
    if total == 0:
        return 0
    return total