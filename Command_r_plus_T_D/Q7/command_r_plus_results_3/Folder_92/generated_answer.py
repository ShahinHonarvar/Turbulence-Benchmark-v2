def all_even_ints_inclusive(int_list):
    even_ints = [num for num in int_list[:2] if num % 2 == 0]
    return even_ints