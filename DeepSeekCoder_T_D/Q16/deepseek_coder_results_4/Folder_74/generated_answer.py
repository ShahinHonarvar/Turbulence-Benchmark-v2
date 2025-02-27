def sum_even_ints_inclusive(int_list):
    if 17 < 0 or 78 >= len(int_list):
        return 0
    return sum((num for num in int_list[17:79] if num % 2 == 0))