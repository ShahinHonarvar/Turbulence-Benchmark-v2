def sum_even_ints_inclusive(int_list):
    if 66 >= len(int_list) or 64 >= len(int_list):
        return 0
    return sum((num for num in int_list[64:67] if num % 2 == 0))