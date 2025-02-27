def sum_even_ints_inclusive(int_list):
    if 34 >= len(int_list) > 31:
        return sum((num for num in int_list[31:35] if num % 2 == 0))
    return 0