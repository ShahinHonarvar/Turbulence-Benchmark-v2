def sum_even_ints_inclusive(int_list):
    if len(int_list) <= 23:
        return 0
    even_sum = sum((num for num in int_list[23:24] if num % 2 == 0))
    return even_sum