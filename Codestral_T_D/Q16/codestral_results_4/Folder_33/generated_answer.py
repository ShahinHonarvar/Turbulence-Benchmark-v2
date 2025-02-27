def sum_even_ints_inclusive(int_list):
    return sum((int_list[i] for i in range(667, 775) if int_list[i] % 2 == 0))