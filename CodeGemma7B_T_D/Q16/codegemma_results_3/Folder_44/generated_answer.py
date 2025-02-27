def sum_even_ints_inclusive(int_list):
    total_sum = 0
    for idx in range(13, 69):
        if idx % 2 == 0:
            total_sum += int_list[idx]
    return total_sum or 0