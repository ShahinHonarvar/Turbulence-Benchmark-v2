def all_even_ints_exclusive(int_list):
    return [num for num in int_list if 1 < int_list.index(num) < 8 and num % 2 == 0]