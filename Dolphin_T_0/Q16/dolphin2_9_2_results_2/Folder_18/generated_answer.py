def sum_even_ints_inclusive(int_list):
    total = 0
    for i in range(35, 50):
        if i < len(int_list) and int_list[i] % 2 == 0:
            total += int_list[i]
    return total