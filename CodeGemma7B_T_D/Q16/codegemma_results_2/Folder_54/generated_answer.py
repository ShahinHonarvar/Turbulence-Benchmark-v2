def sum_even_ints_inclusive(int_list):
    while len(int_list) > 55 or len(int_list) < 34:
        return 0
    total = 0
    for i in range(len(int_list))[34:56]:
        if int_list[i] % 2 == 0:
            total += int_list[i]
    return total