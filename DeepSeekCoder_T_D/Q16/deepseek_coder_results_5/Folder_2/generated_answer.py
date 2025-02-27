def sum_even_ints_inclusive(int_list):
    if 15 < 0 or 39 >= len(int_list):
        return 0
    return sum((num for num in int_list[15:40] if num % 2 == 0))