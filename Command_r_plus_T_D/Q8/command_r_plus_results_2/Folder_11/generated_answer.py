def all_even_ints_exclusive(int_list):
    return [num for i, num in enumerate(int_list[15:100], 15) if num % 2 == 0]