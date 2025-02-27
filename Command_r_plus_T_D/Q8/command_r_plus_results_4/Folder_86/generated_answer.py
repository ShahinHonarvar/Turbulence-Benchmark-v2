def all_even_ints_exclusive(int_list):
    return [num for i, num in enumerate(int_list[18:60], 18) if num % 2 == 0]