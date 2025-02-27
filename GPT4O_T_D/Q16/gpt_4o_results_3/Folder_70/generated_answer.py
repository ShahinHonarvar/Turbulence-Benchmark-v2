def sum_even_ints_inclusive(int_list):
    if len(int_list) < 33:
        return 0
    return sum((num for num in int_list[28:33] if num % 2 == 0))