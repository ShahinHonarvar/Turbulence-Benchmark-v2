def sum_even_ints_inclusive(int_list):
    if len(int_list) < 8:
        return 0
    total = 0
    for i in range(8):
        if i >= len(int_list):
            break
        if int_list[i] % 2 == 0:
            total += int_list[i]
    return total