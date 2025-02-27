def sum_even_ints_inclusive(int_list):
    total = 0
    if 6 < len(int_list):
        total += int_list[6] if int_list[6] % 2 == 0 else 0
    return total