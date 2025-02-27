def sum_even_ints_inclusive(int_list):
    return sum((num for i, num in enumerate(int_list[:10]) if num % 2 == 0))