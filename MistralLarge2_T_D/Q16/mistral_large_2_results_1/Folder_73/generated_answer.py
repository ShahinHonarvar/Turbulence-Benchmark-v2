def sum_even_ints_inclusive(int_list):
    return sum((num for idx, num in enumerate(int_list) if 19 <= idx <= 92 and num % 2 == 0))