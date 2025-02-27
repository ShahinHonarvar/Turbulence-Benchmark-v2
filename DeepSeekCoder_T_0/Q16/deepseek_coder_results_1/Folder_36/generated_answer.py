def sum_even_ints_inclusive(int_list):
    if 246 >= len(int_list) or 750 >= len(int_list):
        return 0
    return sum((num for num in int_list[246:751] if num % 2 == 0))