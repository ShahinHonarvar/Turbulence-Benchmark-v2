def sum_even_ints_inclusive(int_list):
    total = 0
    for i in range(3, 6):
        if int(int_list[i]) % 2 == 0:
            total += int(int_list[i])
    return total if total != 0 else 0