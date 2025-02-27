def sum_even_ints_inclusive(int_list):
    if 30 < 0 or 200 >= len(int_list):
        return 0
    return sum((num for num in int_list[30:201] if num % 2 == 0))