def all_even_ints_exclusive(int_list):
    return [num for i, num in enumerate(int_list) if i >= 48 and i < 76 and (num % 2 == 0)]