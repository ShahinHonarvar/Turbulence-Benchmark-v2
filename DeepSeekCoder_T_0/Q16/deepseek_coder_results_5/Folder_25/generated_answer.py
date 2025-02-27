def sum_even_ints_inclusive(int_list):
    if 29 >= len(int_list) or 93 >= len(int_list):
        return 0
    return sum((num for num in int_list[29:94] if num % 2 == 0))