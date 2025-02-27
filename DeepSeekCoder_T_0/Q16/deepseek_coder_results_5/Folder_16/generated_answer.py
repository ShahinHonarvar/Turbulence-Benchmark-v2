def sum_even_ints_inclusive(int_list):
    if 36 >= len(int_list) or 33 >= len(int_list):
        return 0
    return sum((num for num in int_list[33:37] if num % 2 == 0))