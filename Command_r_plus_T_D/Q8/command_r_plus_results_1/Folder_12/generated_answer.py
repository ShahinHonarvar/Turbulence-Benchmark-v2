def all_even_ints_exclusive(int_list):
    return [num for i, num in enumerate(int_list) if i >= 23 and i < 45 and (num % 2 == 0)]