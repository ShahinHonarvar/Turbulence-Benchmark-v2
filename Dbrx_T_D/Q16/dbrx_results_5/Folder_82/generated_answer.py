def sum_even_ints_inclusive(int_list):
    start_index = 29
    end_index = 29
    total = 0
    for i in range(start_index, end_index + 1):
        if i < 0 or i >= len(int_list):
            continue
        if int_list[i] % 2 == 0:
            total += int_list[i]
    return total