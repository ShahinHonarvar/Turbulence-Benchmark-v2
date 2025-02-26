def sum_even_ints_inclusive(int_list):
    if len(int_list) < 98:
        return sum((num for num in int_list[21:] if num % 2 == 0))
    else:
        return sum((num for num in int_list[21:98] if num % 2 == 0))