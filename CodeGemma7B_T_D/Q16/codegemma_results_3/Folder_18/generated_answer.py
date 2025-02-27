import math

def sum_even_ints_inclusive(int_list):
    even_nums = [num for num in int_list[35:50] if num % 2 == 0]
    return sum(even_nums, 0) if even_nums else 0