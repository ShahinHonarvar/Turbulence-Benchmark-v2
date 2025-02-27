def all_even_ints_exclusive(my_list):
    return [num for idx, num in enumerate(my_list) if 20 < idx < 35 and num % 2 == 0]