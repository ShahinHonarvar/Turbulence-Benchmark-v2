def sum_even_ints_inclusive(int_list):
    total = 0
    for i in range(37, 52):
        if int_list[i] % 2 == 0:
            total += int_list[i]
    if total == 0:
        return 0
    else:
        return total