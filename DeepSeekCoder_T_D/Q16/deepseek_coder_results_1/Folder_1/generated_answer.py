def sum_even_ints_inclusive(int_list):
    if 31 < 0 or 72 >= len(int_list):
        return 0
    return sum((num for num in int_list[31:73] if num % 2 == 0))